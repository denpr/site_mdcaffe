const center_img = document.querySelector('.inform__center_block');
const inf_container = document.querySelector('.inform_layer__container')
const first_block = document.querySelector('#first_block')
const second_block = document.querySelector('#second_block')
var center_show = true
var second_block_show = true
let second_block_remove_width = 580

if (document.documentElement.clientWidth < 1000) {
    center_img.remove()
    center_show = false
} else {
    center_show = true
}
if (document.documentElement.clientWidth < second_block_remove_width) {
  second_block.remove()
  second_block_show = false
} else {
  second_block_show = true
}



window.onresize = check_width;
function check_width(){
    if (document.documentElement.clientWidth < 1000 && center_show == true) {
        center_img.remove()
        center_show = false
    } else if (document.documentElement.clientWidth > 1000 && center_show == false){
        first_block.after(center_img)
        center_show = true
    } 
    if (document.documentElement.clientWidth < second_block_remove_width && second_block_show == true) {
        second_block.remove()
        second_block_show = false
    } else if (document.documentElement.clientWidth > second_block_remove_width && second_block_show == false){
      first_block.after(second_block)
      second_block_show = true
    } 
}

initImg('#test img', [
    'https://newsroom.kz/wp-content/uploads/2020/12/1-brazil-dia-1536x1024.jpg',
    'https://wp.sieuthicafe.vn/wp-content/uploads/2021/08/ethiopia-01.jpg',
    'https://cf80556.tmweb.ru/upload/iblock/656/african_savannahwidescreen_wallpapers_1440x900.jpeg'
  ]); 
  
  function initImg(selector, srcArr) {
    const img = document.querySelector(selector); 
    Object.assign(img, {
      buf: Object.assign(new Image(), { img }), 
      srcArr: [...srcArr], 
      changeInterval: 5e3,
      bufIdx: 0,
      change: function () {
        this.style.animationName = 'img-in'; 
        this.src = this.buf.src || this.nextImage(); 
        this.buf.src = this.nextImage(); 
      }, 
      nextImage: function () {
        this.bufIdx = ++this.bufIdx < this.srcArr.length ? this.bufIdx : 0;
        return this.srcArr[this.bufIdx];
      }
    }); 
    img.buf.addEventListener('load', loadHandler); 
    img.addEventListener('animationend', animEndHandler); 
    img.change(); 
    return img; 
  
    function loadHandler() {
      setTimeout(
        () => this.img.style.animationName = 'img-out', 
        this.img.changeInterval 
      ); 
    }
    function animEndHandler({ animationName }) {
      if (animationName === 'img-out') 
        this.change(); 
    }
  }