const anim_time = 0.5;
const logo_big_width = 160;
const logo_big_hight = 110;
const logo_small_width = 100;
const logo_small_height = 60;

const main_header = document.querySelector('.header');
const main_header_inner = document.querySelector('.header__row')
const logo_class = document.querySelector('.header__logo')
const nav = document.querySelector('nav')    
    window.addEventListener('scroll', function () {
        if (this.window.scrollY > 200) {
            // Здвигаем и затемняем лолготип
            width = main_header.offsetWidth / 2 - 90;
            logo_class.style.transform = 'translate(-' + width + 'px, -50px) scale(0.2)';
            logo_class.style.opacity = '0';
            logo_class.style.transition = 'all ' + anim_time + 's;'

            // Текст
            if (!this.document.querySelector('.logo-text')) {
                let wrap = this.document.createElement('div')
                wrap.className = 'small-wrap'

                let h1 = document.createElement('div')
                h1.className = 'logo-text fade-in'
                h1.innerHTML = '<div>Moby Dick Caffe</div>'
                wrap.prepend(h1)
                
                let img_small = this.document.createElement('div')
                img_small.className = 'logo-img-small fade-in'
                var img = document.createElement('img');
                img.src = small_logo_url
                img.style.paddingTop = '18px'
                img.style.paddingRight = '10px'
                img.style.width = '80px'
                img.style.height = '30px'
                img.style.opacity = '0.9'
                wrap.prepend(img)
                main_header_inner.prepend(wrap)
                main_header.classList.add('_small')
                main_header_inner.classList.add('_small')
            }  
        } else {
            if (this.document.querySelector('.logo-text')) {
                this.document.querySelector('.small-wrap').remove()
            }
            width = main_header.offsetWidth / 2 - 90;
            // str = 'translate(' + width + 'px, 0px)';
            str = 'translate(0px, 0px)';
            console.log(str)
            logo_class.style.transform = str;
            logo_class.style.opacity = '1'
            logo_class.style.transition = 'all ' + anim_time + 's'
            
            main_header.classList.remove('_small')
            main_header_inner.classList.remove('_small')
            // logo_class.classList.remove('_small')
        }
    });