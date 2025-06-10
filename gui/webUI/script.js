// جلب العنصر <tbody>
const shortcutBody = document.getElementById("shortcut-body");


console.log(shortcutBody);
// جلب البيانات من API
fetch("http://127.0.0.1:4000/")
  .then((response) => {
    if (!response.ok) throw new Error("Network response was not ok");
    return response.json();
  })
  .then((data) => {
    // تفريغ الجدول أولاً (لو كنت بتحدثه لاحقًا)
    shortcutBody.innerHTML = "";

    // إدخال صف لكل اختصار
    data.forEach((item) => {
      const row = document.createElement("tr");

      const shortcutCell = document.createElement("td");
      shortcutCell.textContent = item.shortcut;

      const actionCell = document.createElement("td");
      actionCell.textContent = item.action;

      row.appendChild(shortcutCell);
      row.appendChild(actionCell);

      shortcutBody.appendChild(row);
    });
  })
  .catch((error) => {
    console.error("Error fetching shortcuts:", error);
  });
