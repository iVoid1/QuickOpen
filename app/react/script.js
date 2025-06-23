// جلب العنصر <tbody>
const shortcutBody = document.getElementById("shortcut-body");

function fetchingData() {
  // جلب البيانات من API
  fetch("http://127.0.0.1:3000/commands")
    .then((response) => {
      if (!response.ok) throw new Error("Network response was not ok");
      return response.json();
    })
    .then((data) => {
      // تفريغ الجدول أولاً (لو كنت بتحدثه لاحقًا)
      shortcutBody.innerHTML = "";
  
      // إدخال صف لكل اختصار
      data.forEach((item) => {
        console.log(item);
      });
    })
    .catch((error) => {
      console.error("Error fetching shortcuts:", error);
    });
}

function addShortcut() {
  const shortcut = document.getElementById("new-shortcut").value;
  const command = document.getElementById("new-command").value;

  fetch("http://localhost:3000/command/add", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ shortcut, command })
  })
  .then(res => res.json())
  .then(data => {
    console.log("Updated config:", data);
    // تحديث القائمة تلقائيًا
    location.reload();
  });
}

