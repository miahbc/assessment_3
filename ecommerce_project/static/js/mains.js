
document.getElementById('search-form').addEventListener('submit', (event)=>{
    event.preventDefault()

    const searchInput = document.getElementById('product')

    // send a GET request to /products on our server, passing searchInput.value as data.
    axios.get('/products', {params:{query: searchInput.value}})

    // handle the response from the server
    .then((response)=>{
        console.log('response?')
        console.log(response)

        newImage = document.createElement('img')
        newImage.src = response.data.url

        const soldOut = document.createElement('h1')
        soldOut.innerText = "Sorry, we don't offer this item!"

        const hr = document.createElement('hr')
        document.body.appendChild(newImage)
        document.body.appendChild(soldOut)
        document.body.appendChild(hr)

    })
    // console.log(searchInput.value)
})