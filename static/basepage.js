function increaseCount(a, b) {
    var input = b.previousElementSibling;
    var value = parseInt(input.value, 10);
    value = isNaN(value) ? 0 : value;
    value++;
    input.value = value;
}

function decreaseCount(a, b) {
    var input = b.nextElementSibling;
    var value = parseInt(input.value, 10);
    if (value > 1) {
        value = isNaN(value) ? 0 : value;
        value--;
        input.value = value;
    }
}

function menu_list() {
    var swiper_wrapper = document.getElementById("swiper-wrapper-3c5c74a883983131");
    var json = {
        'pizza': {'africano_pizza': 50000, 'akbar_pizza': 30000},
        'salad': {'akbar_salad': 12000, 'sezar': 5000},
        'hotdrink': {'hotchaklet': 12000, 'masala': 5000}
    }
    // // var json = $.getJSON("http://127.0.0.1:5000/menus/list/")['responseJSON']
    // console.log(json)
    // console.log(json.toJSON)
    for (let category in json) {
        let swiper_slide = document.createElement("div")
        swiper_slide.className = "swiper-slide"
        swiper_slide.setAttribute("role", "group")
        swiper_slide.setAttribute("style", "width: 15%; margin-right: 5%;")
        swiper_wrapper.append(swiper_slide)

        let modal = document.createElement("div")
        modal.setAttribute("data-toggle", "modal")
        modal.setAttribute("data-target", "#" + category)
        swiper_slide.append(modal)

        let menu = document.createElement("div")
        menu.className = "menu"
        modal.append(menu)

        let img_div = document.createElement("div")
        img_div.className = "row"
        menu.append(img_div)

        let img = document.createElement("img")
        img.className = "menu_img"
        img.setAttribute("src", "images/icon/" + category + ".png")
        img_div.append(img)

        let stars = document.createElement("div")
        stars.className = "row star_rating"
        menu.append(stars)

        for (let j = 1; j <= 5; j++) {
            let span = document.createElement("span")
            span.className = "fa fa-star checked"
            stars.append(span)
        }

        let name_of_category = document.createElement("div")
        name_of_category.className = "row menu_item"
        name_of_category.innerText = category
        menu.append(name_of_category)

        let content_of_modal = document.getElementById("content_of_modal")

        let column = document.createElement("div")
        column.className = "col-10"
        content_of_modal.append(column)

        let modal_item = document.createElement("div")
        modal_item.className = "modal fade"
        modal_item.id = category
        column.append(modal_item)

        let modal_dialog = document.createElement("div")
        modal_dialog.className = "modal-dialog modal-md"
        modal_item.append(modal_dialog)

        let modal_content = document.createElement("div")
        modal_content.className = "modal-content bg-light"
        modal_dialog.append(modal_content)

        let modal_body = document.createElement("div")
        modal_body.className = "modal-body"
        modal_content.append(modal_body)

        let ul = document.createElement("ul")
        ul.className = "list-group font-weight-bolder"
        modal_body.append(ul)

        let li_title = document.createElement("li")
        li_title.className = "list-group-item  title-menu-sub"
        li_title.innerText = category
        ul.append(li_title)

        for (let modal_content in json[category]) {

            let li = document.createElement("li")
            li.className = "list-group-item"
            ul.append(li)

            let menu_sub = document.createElement("div")
            menu_sub.className = "row menu-sub"
            li.append(menu_sub)

            let item_sub = document.createElement("div")
            item_sub.className = "col-3 item-sub"
            menu_sub.append(item_sub)

            let item_img = document.createElement("img")
            item_img.className = "item-img"
            item_img.setAttribute("src", `images/menu_img/${category}/${modal_content}.jpg`)
            item_sub.append(item_img)

            let name_of_item = document.createElement("div")
            name_of_item.className = "col-4 item-sub title-menu-sub-item"
            name_of_item.innerText = modal_content
            menu_sub.append(name_of_item)

            let price_of_item = document.createElement("div")
            price_of_item.className = "col-2 item-sub title-menu-sub-item"
            price_of_item.innerText = json[category][modal_content]
            menu_sub.append(price_of_item)

            let img_item = document.createElement("div")
            img_item.className = "col-3 item-sub"
            menu_sub.append(img_item)

            let add_cart = document.createElement("span")
            add_cart.className = "add-cart"
            img_item.append(add_cart)

            let img_plus = document.createElement("img")
            img_plus.className = "add-cart-icon"
            img_plus.setAttribute("src", "icon/add.png")
            add_cart.append(img_plus)

        }

    }
}