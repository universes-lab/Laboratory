async function updateInfoPanel() {
  const sources = ['ceo', 'chief', 'doctor'];

  for (const source of sources) {
    try {
      const response = await fetch(`/api/info/${source}`);
      if (!response.ok) continue;

      const data = await response.json();
      const element = document.getElementById(`${source}-info`);

      if (element && data.content) {
        // Простое форматирование: переносы строк (уже обрабатываются CSS white-space: pre-wrap)
        element.textContent = data.content;
      }
    } catch (error) {
      console.error(`Ошибка загрузки ${source}:`, error);
    }
  }
}

// Обновление каждые 60 секунд (чтобы не спамить)
let infoUpdateInterval = setInterval(updateInfoPanel, 60000);

// Инициализация при загрузке
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', updateInfoPanel);
} else {
  updateInfoPanel();
}
