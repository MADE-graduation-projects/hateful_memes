var res_str = '';


function start_work(){
		chrome.tabs.executeScript({code: `
		(function(){
	var result = '';
	var tableborder = document.getElementsByClassName('tableborder')[0];
	var tables = tableborder.getElementsByTagName('table');
	for(var i = 0; i < tables.length; i++){
		var id = tables[i].getAttribute('id');
		if(id == null)
			continue;
		//console.log(id);
		//if(id.includes('p_row'))
		//	result += id + ' ';
		
		var nick = tables[i].getElementsByClassName('normalname')[0].innerText;
		var autor_link = tables[i].getElementsByClassName('postdetails')[0].getElementsByTagName('a')[0].href;
		
		var postcolor = tables[i].getElementsByClassName('postcolor')[0];

		var image_links = postcolor.getElementsByTagName('a');
		if(image_links.length > 0){
		
			console.log(postcolor.innerText);
			var image_link = image_links[0].href;
			result += nick + "|" + image_link + "*";
		}
		else{
			var image_links = postcolor.getElementsByTagName('img');
			if(image_links.length > 0){
			
				console.log(postcolor.innerText + image_links[0].src);
				var image_link = image_links[0].src;
				result += nick + "|" + image_link + "*";
			}
			else{
				continue;
			}			
		}
	}
	return result;
})()

		`},
		function(result) { res_str += result[0]; console.info(result[0]); pages(); } );
		
	
}
			

document.getElementById('start').onclick = function(evnt) {
	res_str = '';
	document.getElementById('url').value = res_str;	
	
	start_work();/*
	var tableborder = document.getElementByClassName('tableborder');
	var tables = tableborder.getElementsByTagName('table');
	for(var i = 0; i < tables.length; i++){
		result += i + ' ' + tables[i].getAttribute('id');
	}*/
	//[2].getElementsByClassName('postcolor')[0].getElementsByTagName('a')
	//var url = document.getElementById('url').value;

}

document.getElementById('pages').onclick = function(evnt) {
	pages();

}



function pages(){
		chrome.tabs.executeScript({code: `
		(function(){
	var links = document.getElementsByTagName('b');
	var page = links[0];
	for(var i = 0; i < links.length; i++){
		page = links[i];
		if(page.innerText.includes('[') && page.innerText.includes(']')){
		//if(page.getAttribute('title') == 'Переход на страницу...'){//page.href.indexOf('#') == page.href.length - 1 || 
			console.log(i, page.innerText, page.getAttribute('title'), page.href);
			break;
		}
	}
	console.log(links.length);
	console.log(i, page.nextElementSibling);

	if(page.nextElementSibling == null || page.nextElementSibling.innerHTML.includes('.gif')){
		console.log('last page');
		return false;
	}

	else{
		console.log('go to next page');
		page.nextElementSibling.click();
		return true;
	}


})()

		`},
		function(result) {
			if(result[0]){
				console.info('yes');
				setTimeout(start_work, 3000);
			}
			else{
				document.getElementById('url').value = res_str;
				console.info('end');
			}
				
			}
		);
		
	
	
}


document.getElementById('save').onclick = saveDynamicDataToFile;

function saveDynamicDataToFile() {

    var text = document.getElementById("url").value;
	
  var a = document.getElementById("a");
  var file = new Blob([text], {type: 'text/plain'});
  a.href = URL.createObjectURL(file);
  a.download = name;
}

function download(text, name, type) {
  var a = document.getElementById("a");
  var file = new Blob([text], {type: type});
  a.href = URL.createObjectURL(file);
  a.download = name;
}