tvar flag = false
function displayP(){
	var content = document.getElementByID('con');
	var btn = document.getElementByID('btn');
	index = 0;
	btn.click=function(){
		content[(btn.index(this))].style.display= 'block';
		console.log(btn);
	};
	
	
};