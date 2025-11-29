const form = document.getElementById('upload-form');
const resultEl = document.getElementById('result');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  resultEl.textContent = 'Uploading...';
  const fileInput = document.getElementById('file');
  const title = document.getElementById('title').value;
  if (!fileInput.files.length) {
    resultEl.textContent = 'Please pick a video file.';
    return;
  }

  const file = fileInput.files[0];
  const fd = new FormData();
  fd.append('file', file);
  fd.append('title', title);

  try {
    const uploadRes = await fetch('http://localhost:8000/api/upload', {
      method: 'POST',
      body: fd,
    });
    const uploadJson = await uploadRes.json();
    if (!uploadRes.ok) {
      resultEl.textContent = JSON.stringify(uploadJson, null, 2);
      return;
    }

    // collect selected platforms
    const platforms = Array.from(document.querySelectorAll('input[name=platform]:checked')).map(el => el.value);

    const publishRes = await fetch('http://localhost:8000/api/publish', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id: uploadJson.id, platforms }),
    });
    const publishJson = await publishRes.json();
    resultEl.textContent = 'Success:\n' + JSON.stringify({ upload: uploadJson, publish: publishJson }, null, 2);
  } catch (err) {
    resultEl.textContent = String(err);
  }
});
