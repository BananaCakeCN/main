if (!window.document.documentMode==false) {
    document.getElementsByClassName('background-img')[0].innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" style="overflow: hidden;" height="100%"><defs><filter id="blur"><feGaussianBlur stdDeviation="8"></feGaussianBlur></filter></defs><image filter="url(&quot;#blur&quot;)" x="0%" width="1920px" height="1080px" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="https://bananacake.top/img/Fr5Ri464JOjH8180Z029lrRHivfm.jpg"></image></svg><div style="background-color: rgba(221, 221, 221, 0.8); width: 100%; height: 100%; position: absolute; top: 0;"></div>'
    document.getElementsByClassName('background-img')[0].style.cssText = 'background: none; filter: none;'
    document.getElementsByClassName('tab')[0].style.cssText = 'background-color: rgba(153, 153, 153, 0.27);'
    if(location.href.split('/')[location.href.split('/').length-1]=== 'images.html'||location.href.split('/')[location.href.split('/').length-1]=== 'images'){
        location.href = 'http://internetexp.bananacake.top/images'
    }
}
