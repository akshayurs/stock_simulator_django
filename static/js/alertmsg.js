var close = document.getElementsByClassName('closebtn')
var i

for (i = 0; i < close.length; i++) {
  close[i].onclick = function () {
    var div = this.parentElement
    div.style.opacity = '0'
    setTimeout(function () {
      div.style.display = 'none'
    }, 600)
  }
}
const alertmsgs = document.querySelectorAll('.alertmsg')
alertmsgs?.forEach((div) => {
  setTimeout(function () {
    div.style.opacity = '0'
  }, 4000)
  setTimeout(function () {
    div.style.display = 'none'
  }, 5000)
})
