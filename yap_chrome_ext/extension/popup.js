var result = '';

document.getElementById('start').onclick = function(evnt) {
	result = '';
	document.getElementById('result').value = result;	
	startWork();
}

function startWork(){
	chrome.tabs.query({active: true, lastFocusedWindow: true}, collectImages);//
}

function collectImages(tabs){
	var url = tabs[0].url;
	document.getElementById('file_name').value = url.substring(url.lastIndexOf('/') + 1);

	chrome.tabs.executeScript({
		code: `
		(function(){
			var res = '';
			//var topicName = document.getElementById('main-title').innerText;
			var tableborder = document.getElementsByClassName('tableborder')[0];
			var tables = tableborder.getElementsByTagName('table');
			for(var i = 0; i < tables.length; i++){
				var id = tables[i].getAttribute('id');
				if(id == null)
					continue;
		
				var nick = tables[i].getElementsByClassName('normalname')[0].innerText;
				var autorLink = tables[i].getElementsByClassName('postdetails')[0].getElementsByTagName('a')[0].href;			
				var postcolor = tables[i].getElementsByClassName('postcolor')[0];
				var imageLinks = postcolor.getElementsByTagName('a');
				
				if(imageLinks.length > 0){
					var imageLink = imageLinks[0].href;
					res += nick + "|" + imageLink + "*";
				}
				else{
					var imageLinks = postcolor.getElementsByTagName('img');
					if(imageLinks.length > 0){
						var imageLink = imageLinks[0].src;
						res += nick + "|" + imageLink + "*";
					}
					else{
						continue;
					}			
				}
			}
			return res;
		})()`},
		
		function(res) {
			result += res[0] + '*';
			goToNextPage();
		}
	);
}

function goToNextPage(){
	chrome.tabs.executeScript({
		code: `
		(function(){
			var links = document.getElementsByTagName('b');
			var page = links[0];
			for(var i = 0; i < links.length; i++){
				page = links[i];
				
				if(page.innerText.includes('[') && page.innerText.includes(']')){
					break;
				}
			}

			if(page.nextElementSibling == null || page.nextElementSibling.innerHTML.includes('.gif')){
				return false;
			}
			else{
				page.nextElementSibling.click();
				return true;
			}
		})()`},
		
		function(res) {
			if(res[0]){
				setTimeout(startWork, 3000);
			}
			else{
				document.getElementById('result').value = result;
				saveDataToFile();
			}				
		}
	);
}

function saveDataToFile() {
	var text = document.getElementById("result").value;
	var fileName = document.getElementById('file_name').value;
	var file = new Blob([text], {type: 'text/plain'});

	chrome.downloads.download({
		url: URL.createObjectURL(file),
		filename: 'files/' + fileName
	});
}
