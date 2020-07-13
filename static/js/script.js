
let add_attribute=function(attribute,value)
{
    url=location.href
    if(url.includes('?'))
    {
        comined=attribute+'=\\d'
        console.log(comined)
        regex=new RegExp(comined)
        let result=url.match(regex)
        if(result ==null)
            url=`${url}&${attribute}=${value}`
        else
        {
            url=url.replace(regex,`${attribute}=${value}`)
        }
    }
    else
        url=`${url}?${attribute}=${value}`
    location.href=url
}

// managing active classes
qs=document.querySelectorAll('.js-cls')

qs.forEach((item,index)=>
{
    item.addEventListener('click',(target)=>
    {
        qs.forEach((inner)=>{
            inner.classList.remove('active')
        })
        item.classList.add('active')
        console.log(item.classList)
    })
})

function fn1()
{
    vp_one=document.querySelector('#vp1')
    vp_two=document.querySelector('#vp2')
    vp_one.style.display="none"
    vp_two.style.display="block"
    fn2()
}
function fn2()
{
    shop_rating_item=document.querySelector('#shop_rating_id')
    shop_rating=Number(shop_rating_item.textContent)
    rating_input=document.querySelector('#rating_input')
    js_stars=document.querySelectorAll('.js-star')
    js_stars.forEach((star,index)=>
    {
        if(index+1<=shop_rating)
        {
            star.classList.remove('inactive-star')
            star.classList.add('active-star')
        }
    })
    rating_input.value=shop_rating
}

js_stars=document.querySelectorAll('.js-star')
js_stars.forEach((star,index)=>
{
    star.addEventListener('click',()=>
    {
        js_stars.forEach((temp)=>
        {
            temp.classList.remove('active-star')
            temp.classList.add('inactive-star')
        })
        js_stars.forEach((new_star,new_index)=>
        {
            if(new_index<=index)
            {
                new_star.classList.remove('inactive-star')
                new_star.classList.add('active-star')
            }
        })
        rating_input.value=index+1 
    })
})

function show_address()
{
    new_address=document.querySelector("#new_address")
    address_label=document.querySelector("#address_label")
    address_icon=document.querySelector('#address_icon')
    if(new_address.style.display == 'none')
    {
    new_address.style.display="flex";
    address_icon.classList.remove('fa-plus-circle')
    address_icon.classList.add('fa-minus-circle')
    address_label.textContent="use existing addresses"
    remove_btn_success()
    }
    else
    { 
    new_address.style.display="none"
    address_icon.classList.remove('fa-minus-circle')
    address_icon.classList.add('fa-plus-circle')
    address_label.textContent="add new address"
    }

}

js_forms = document.querySelectorAll("#js_form")
js_forms.forEach((js_form)=>
{
    js_form.addEventListener('click',()=>
    {
        js_form.value=''
    })
})
function remove_btn_success()
{
    existing_address=document.querySelectorAll(".existing-address")
    address_flag=document.querySelector("#address_flag")
    existing_address.forEach((address)=>
    {
        address.classList.remove('btn-success')
        address.classList.add('btn-primary')
        address.textContent="Deliver Here"
        address_flag.value="0"
    })
}

function existing_address_func()
{
    existing_address=document.querySelectorAll(".existing-address")
    address_flag=document.querySelector("#address_flag")
    existing_address.forEach((address)=>
    {
        address.addEventListener('click',()=>
        {
            address_card=address.parentElement
            address_id=address_card.querySelector('#address_id')
            remove_btn_success()
            new_address=document.querySelector("#new_address")
            if(new_address.style.display =="flex")
                show_address()
            address.classList.remove('btn-primary')
            address.classList.add('btn-success')
            address.textContent="Address Selected!"
            address_flag.value=address_id.textContent
        })
    })
}
existing_address_func()


