const imageInput = document.getElementById('image');
const imagePreview = document.getElementById('imagePreview');
const previewImg = imagePreview.querySelector('.preview-img');
const removeBtn = document.getElementById('removeImage');

imageInput.addEventListener('change', function() {
  const file = this.files[0];
  if (file) {
    const reader = new FileReader();
    reader.addEventListener('load', function() {
      previewImg.setAttribute('src', this.result);
      previewImg.style.display = 'block';
      removeBtn.style.display = 'inline-block';
    });
    reader.readAsDataURL(file);
  }
});

removeBtn.addEventListener('click', function() {
  imageInput.value = '';
  previewImg.setAttribute('src', '');
  previewImg.style.display = 'none';
  removeBtn.style.display = 'none';
});
