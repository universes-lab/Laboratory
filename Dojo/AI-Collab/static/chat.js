document.addEventListener('DOMContentLoaded', () => {
  const userInput = document.getElementById('userInput');
  const chatLogs = document.querySelectorAll('.chat-log');

  const leftChatLog = chatLogs[0];
  const rightChatLog = chatLogs[1];
  let currentLeftChatModel = 'chief';
  let currentRightChatModel = 'ceo';
  let currentSessionId = null;
  let lastClickedSide = 'left';
  let dynamicModelMapping = {};

  // Загрузка названия текущего проекта
  async function loadCurrentProjectName() {
    try {
      const response = await fetch('/api/project/current');
      if (!response.ok) return;
      const data = await response.json();
      const projectNameEl = document.getElementById('current-project-name');
      if (
        projectNameEl &&
        data.project_name &&
        data.project_name !== 'Проект не выбран'
      ) {
        projectNameEl.textContent = `| ${data.project_name}`;
        projectNameEl.title = `Текущий проект: ${data.project_name}`;
      }
    } catch (error) {
      console.error('Ошибка загрузки проекта:', error);
    }
  }

  // Управление информ-окном
  function showInfoPanel() {
    const infoPanel = document.getElementById('info-panel');
    const gcbWindow = document.getElementById('gcb-window');
    if (infoPanel) infoPanel.classList.add('active');
    if (gcbWindow) gcbWindow.classList.remove('active');
  }

  function showGCBQueue() {
    const infoPanel = document.getElementById('info-panel');
    const gcbWindow = document.getElementById('gcb-window');
    if (infoPanel) infoPanel.classList.remove('active');
    if (gcbWindow) gcbWindow.classList.add('active');
    updateGCBQueue();
  }

  // Загрузка контента в информ-окно
  async function loadInfoContent(infoType, additionalData = null) {
    try {
      const url = additionalData
        ? `/api/info/${infoType}?${new URLSearchParams(additionalData).toString()}`
        : `/api/info/${infoType}`;

      const response = await fetch(url);
      if (!response.ok) throw new Error(`HTTP ${response.status}`);

      const html = await response.text();
      const infoPanel = document.getElementById('info-panel');
      if (infoPanel) {
        infoPanel.innerHTML = html;
        showInfoPanel();
      }
    } catch (error) {
      console.error(`Ошибка загрузки контента ${infoType}:`, error);
      const infoPanel = document.getElementById('info-panel');
      if (infoPanel) {
        infoPanel.innerHTML = `<div style="padding: 20px; color: #e74c3c;">Ошибка загрузки: ${error.message}</div>`;
        showInfoPanel();
      }
    }
  }

  let enterCount = 0;
  let lastEnterTime = 0;

  const mentionChiefBtn = document.getElementById('mentionChiefBtn');
  const mentionCeoBtn = document.getElementById('mentionCeoBtn');
  const topChiefBtn = document.querySelector('.chief-top');
  const topCeoBtn = document.querySelector('.ceo-top');
  const topGeminiBtn = document.querySelector('.gemini-top');
  const topDoctorBtn = document.querySelector('.doctor-top');

  const sendBtnLeft = document.getElementById('sendBtnLeft');
  const sendBtnRight = document.getElementById('sendBtnRight');

  function updateActiveUI(side, specificRole = null) {
    lastClickedSide = side;

    let roleToApply = specificRole;
    if (roleToApply === null) {
      const model =
        side === 'left' ? currentLeftChatModel : currentRightChatModel;
      if (model === 'chief') roleToApply = 'chief';
      else if (model === 'gemini_direct') roleToApply = 'gemini';
      else if (model === 'ceo') roleToApply = 'ceo';
      else if (model === 'doctor') roleToApply = 'doctor';
    }

    // Сброс всех классов и теней
    if (mentionChiefBtn)
      mentionChiefBtn.classList.remove('chief-active', 'inactive');
    if (mentionCeoBtn) mentionCeoBtn.classList.remove('ceo-active', 'inactive');
    [topChiefBtn, topCeoBtn, topGeminiBtn, topDoctorBtn].forEach((btn) => {
      if (btn) {
        btn.style.boxShadow = 'none';
        btn.style.background = '#95a5a6'; // Серый цвет для неактивных кнопок
      }
    });

    // Логика подсветки конкретной роли
    if (roleToApply === 'chief' && topChiefBtn) {
      topChiefBtn.style.background = 'linear-gradient(135deg,#4a6fa5,#2e4a7a)';
      topChiefBtn.style.boxShadow = '0 0 10px #4a6fa5';
      if (mentionChiefBtn) mentionChiefBtn.classList.add('chief-active');
      if (mentionCeoBtn) mentionCeoBtn.classList.add('inactive');
    } else if (roleToApply === 'gemini' && topGeminiBtn) {
      topGeminiBtn.style.background = 'linear-gradient(135deg,#4a6fa5,#2e4a7a)';
      topGeminiBtn.style.boxShadow = '0 0 10px #4a6fa5';
      if (mentionChiefBtn) mentionChiefBtn.classList.add('chief-active');
    } else if (roleToApply === 'ceo' && topCeoBtn) {
      topCeoBtn.style.background = 'linear-gradient(135deg,#2d8f4a,#1a5c2e)';
      topCeoBtn.style.boxShadow = '0 0 10px #2d8f4a';
      if (mentionCeoBtn) mentionCeoBtn.classList.add('ceo-active');
      if (mentionChiefBtn) mentionChiefBtn.classList.add('inactive');
    } else if (roleToApply === 'doctor' && topDoctorBtn) {
      topDoctorBtn.style.background = 'linear-gradient(135deg,#2d8f4a,#1a5c2e)';
      topDoctorBtn.style.boxShadow = '0 0 10px #2d8f4a';
      if (mentionCeoBtn) mentionCeoBtn.classList.add('ceo-active');
    }
  }

  async function loadDynamicModelMapping() {
    try {
      const response = await fetch('/api/model_mapping');
      const data = await response.json();
      if (data.model_mapping) {
        dynamicModelMapping = data.model_mapping;
        initDashboard();
      }
    } catch (error) {
      console.error('Ошибка загрузки динамического маппинга моделей:', error);
    }
  }

  function initDashboard() {
    const visArea = document.getElementById('gcbQueue');
    if (!visArea) return;

    let html =
      '<h3 style="margin-bottom:10px; color:#2c3e50; border-bottom:2px solid #4a6fa5; padding-bottom:5px;">👥 Состав лаборатории AI-Colab</h3>';
    html +=
      '<div style="display:grid; grid-template-columns: 1fr 1fr; gap:10px;">';

    const depts = [
      { name: 'Отдел A Аналитика', models: ['Флик', 'Флок'], color: '#0d47a1' },
      {
        name: 'Отдел B Локализация',
        models: ['Клик', 'Клак'],
        color: '#1b5e20',
      },
      { name: 'Отдел C Критика', models: ['Чек', 'Чок'], color: '#4a148c' },
      {
        name: 'Отдел D Интеграция',
        models: ['Линк', 'Синх'],
        color: '#e65100',
      },
    ];

    depts.forEach((d) => {
      html += `<div style="border-left: 4px solid ${d.color}; padding:8px; background:#f8f9fa; border-radius:4px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">`;
      html += `<strong style="color:${d.color}; font-size:12px;">${d.name}</strong><br>`;
      d.models.forEach((m) => {
        const modelInfo = dynamicModelMapping[m];
        const modelId = modelInfo ? modelInfo.model_id : 'local';
        const shortId = modelId.split('/').pop();
        html += `<span style="font-size:11px; color:#444;">• ${m} <span style="color:#7f8c8d; font-size:10px;">(${shortId})</span></span><br>`;
      });
      html += '</div>';
    });

    html += '</div>';
    visArea.innerHTML = html;
  }

  function addMessage(
    chatLog,
    sender,
    message,
    pairId = null,
    modelData = null,
  ) {
    const msgDiv = document.createElement('div');
    msgDiv.className = 'msg-bubble';
    msgDiv.style.marginBottom = '8px';
    msgDiv.style.padding = '8px';
    msgDiv.style.borderRadius = '4px';
    msgDiv.style.background = sender.includes('Вы') ? '#e3f2fd' : '#f5f5f5';

    let displayName = sender;
    if (sender === 'AI' && modelData) {
      const localModels = ['chief', 'ceo', 'doctor'];
      if (localModels.includes(modelData.key)) {
        displayName = modelData.roleName || modelData.key;
      } else {
        const shortModelId = modelData.modelId
          ? modelData.modelId.length > 30
            ? modelData.modelId.substring(0, 27) + '...'
            : modelData.modelId
          : '';
        displayName = modelData.roleName
          ? `${modelData.roleName} (${shortModelId})`
          : modelData.key;
      }
    }

    // Простая обработка Markdown-подобных жирных шрифтов
    const formattedMessage = message.replace(
      /\*\*(.*?)\*\*/g,
      '<strong>$1</strong>',
    );

    msgDiv.innerHTML = `
            <div style="font-size:11px; color:#7f8c8d; margin-bottom:2px;">${displayName}</div>
            <div style="white-space: pre-wrap;">${formattedMessage}</div>
            ${pairId ? `<button class="soul-btn" style="margin-top:5px;" onclick="analyzePair('${pairId}')">✨ Soul Layer Анализ</button>` : ''}
        `;
    chatLog.appendChild(msgDiv);
    chatLog.scrollTop = chatLog.scrollHeight;
  }

  function handleSystemCommand(command, side) {
    const cmd = command.trim().toLowerCase();
    const chatLog = side === 'left' ? leftChatLog : rightChatLog;

    switch (cmd) {
      case '/help':
        showHelpModal();
        break;
      case '/status':
        addMessage(
          chatLog,
          'Система',
          'Команда /status в разработке. Проверьте .PROJECT_STATE.md',
        );
        break;
      case '/projects':
        addMessage(
          chatLog,
          'Система',
          'Используйте меню "Проекты" в нижней панели.',
        );
        break;
      case '/clear':
        chatLog.innerHTML = `<p class="system-msg">Чат очищен</p>`;
        break;
      case '/mode':
        const model =
          side === 'left' ? currentLeftChatModel : currentRightChatModel;
        addMessage(
          chatLog,
          'Система',
          `Текущая модель: ${model}. Режим работы: AI-Collaboration.`,
        );
        break;
      default:
        console.log('Неизвестная команда:', cmd);
    }
  }

  function showModal(title, content) {
    const modal = document.getElementById('soulModal');
    const modalTitle = document.getElementById('modalTitle');
    const modalBody = document.getElementById('modalBody');
    if (!modal) return;
    modal.style.display = 'block';
    if (modalTitle) modalTitle.textContent = title;
    if (modalBody) modalBody.innerHTML = content;
  }

  function showHelpModal() {
    const helpContent = `
    <div style="font-family: sans-serif;">
        <h4 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 5px;">🎮 Системные команды AI-Colab</h4>
        <div style="margin-top: 15px;">
            <strong>Формат сообщений:</strong>
            <ul style="font-size: 13px;">
                <li><code style="background: #eee; padding: 2px 4px;">[INTRO]</code> — роль модели</li>
                <li><code style="background: #eee; padding: 2px 4px;">[TASK]</code> — задания</li>
            </ul>
        </div>
        <div style="margin-top: 15px;">
            <strong>Команды:</strong>
            <table style="width: 100%; font-size: 13px; border-collapse: collapse;">
                <tr><td style="padding: 3px;"><code>/help</code></td><td>Справка</td></tr>
                <tr><td style="padding: 3px;"><code>/clear</code></td><td>Очистить</td></tr>
                <tr><td style="padding: 3px;"><code>/mode</code></td><td>Режим</td></tr>
            </table>
        </div>
    </div>`;
    showModal('Справка', helpContent);
  }

  window.analyzePair = async function (pairId) {
    if (!currentSessionId) return alert('Сессия не начата');
    const modal = document.getElementById('soulModal');
    const modalBody = document.getElementById('modalBody');
    modal.style.display = 'block';
    modalBody.innerHTML =
      '<div class="system-msg">Анализ качества диалога...</div>';

    try {
      const response = await fetch(
        `/api/session/${currentSessionId}/analyze/${pairId}`,
        { method: 'POST' },
      );
      const data = await response.json();
      if (data.error) {
        modalBody.innerHTML = `<div class="status-failed">${data.error}</div>`;
        return;
      }
      modalBody.innerHTML = `
                <div class="analysis-grid">
                    <div class="analysis-card">
                        <h4>Оценка: ${data.score || 0}/10</h4>
                        <div class="score-container"><div class="score-bar" style="width: ${data.score * 10}%"></div></div>
                    </div>
                    <div class="analysis-card">
                        <h4>Конструктивность: ${data.constructive_competition ? '✅' : '⚠️'}</h4>
                    </div>
                </div>
                <div class="analysis-card" style="margin-top:10px;">
                    <h4>Резюме ШЕФА:</h4>
                    <p>${data.summary || 'Нет данных'}</p>
                </div>`;
    } catch (e) {
      modalBody.innerHTML = 'Ошибка связи с сервером.';
    }
  };

  // WebSocket для Gemini MCP
  let geminiWS = null;
  function connectGeminiWS() {
    if (geminiWS && geminiWS.readyState === WebSocket.OPEN) return;
    addMessage(leftChatLog, 'Система', 'Подключение к Gemini MCP...');
    geminiWS = new WebSocket('ws://127.0.0.1:8765');
    geminiWS.onopen = () => {
      addMessage(leftChatLog, 'Система', '✅ Прямой канал связи установлен.');
      if (topGeminiBtn) topGeminiBtn.style.boxShadow = '0 0 15px #3498db';
    };
    geminiWS.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.type === 'execution_result') {
        const res = data.result;
        let out = res.success ? '✅ Выполнено' : '❌ Ошибка';
        if (res.output)
          out += `\n<pre style="font-size:10px; background:#eee; padding:5px;">${res.output}</pre>`;
        addMessage(leftChatLog, 'Gemini MCP', out);
      }
    };
  }

  async function handleSend(side) {
    updateActiveUI(side);
    const rawValue = userInput.value.trim();
    if (!rawValue) return;

    if (rawValue.startsWith('/')) {
      handleSystemCommand(rawValue, side);
      userInput.value = '';
      return;
    }

    // Очистка от введённых вручную маркеров
    const cleanMessage = rawValue
      .replace(/^\[INTRO\]\s*/i, '')
      .replace(/^\[TASK\]\s*/i, '');
    const fullMessage = '[INTRO] ' + cleanMessage;

    const chatLog = side === 'left' ? leftChatLog : rightChatLog;
    const modelName =
      side === 'left' ? currentLeftChatModel : currentRightChatModel;
    const senderLabel = `Вы (${modelName})`;

    addMessage(chatLog, senderLabel, cleanMessage);
    userInput.value = '';

    let modelKey = modelName;
    if (side === 'left' && modelKey === 'gemini_direct') {
      if (!geminiWS || geminiWS.readyState !== WebSocket.OPEN) {
        connectGeminiWS();
        return;
      }
      // Для консоли отправляем чистую команду БЕЗ [INTRO]
      geminiWS.send(
        JSON.stringify({
          directive: {
            action: 'shell',
            tool: 'direct_command',
            parameters: { command: cleanMessage },
          },
        }),
      );
      return;
    }

    try {
      const response = await fetch('/api/secretary', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: fullMessage,
          side: side,
          model: modelKey,
          session_id: currentSessionId,
        }),
      });
      const data = await response.json();
      if (data.session_id) currentSessionId = data.session_id;
      if (data.response)
        addMessage(chatLog, 'AI', data.response, data.pair_id, data.modelInfo);
      else if (data.error)
        addMessage(chatLog, 'Система', 'Ошибка: ' + data.error);
    } catch (e) {
      addMessage(chatLog, 'Система', 'Ошибка связи с сервером');
    }
  }

  if (sendBtnLeft)
    sendBtnLeft.addEventListener('click', () => {
      lastClickedSide = 'left';
      handleSend('left');
    });
  if (sendBtnRight)
    sendBtnRight.addEventListener('click', () => {
      lastClickedSide = 'right';
      handleSend('right');
    });

  userInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      const now = Date.now();
      if (now - lastEnterTime < 700) enterCount++;
      else enterCount = 1;
      lastEnterTime = now;
      if (enterCount === 2) {
        e.preventDefault();
        handleSend(lastClickedSide);
        enterCount = 0;
      }
    }
  });

  if (topChiefBtn)
    topChiefBtn.addEventListener('click', () => {
      currentLeftChatModel = 'chief';
      updateActiveUI('left', 'chief');
      addMessage(leftChatLog, 'Система', 'Шеф на связи.');
    });
  if (topCeoBtn)
    topCeoBtn.addEventListener('click', () => {
      currentRightChatModel = 'ceo';
      updateActiveUI('right', 'ceo');
      addMessage(rightChatLog, 'Система', 'СЕО на связи.');
    });
  if (topGeminiBtn)
    topGeminiBtn.addEventListener('click', () => {
      currentLeftChatModel = 'gemini_direct';
      updateActiveUI('left', 'gemini');
      addMessage(leftChatLog, 'Система', '[CONSOLE] Готов к исполнению задач.');
      showGCBQueue(); // Показываем очередь GCB
      connectGeminiWS();
    });
  if (topDoctorBtn)
    topDoctorBtn.addEventListener('click', () => {
      currentRightChatModel = 'doctor';
      updateActiveUI('right', 'doctor');
      addMessage(
        rightChatLog,
        'Система',
        'Доктор на связи. Провести внеплановый медосмотр моделей?',
      );
    });

  // Инициализация
  loadCurrentProjectName();
  showInfoPanel(); // Показываем информ-окно по умолчанию

  document.querySelectorAll('.dept-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
      let id = btn.classList.contains('dept-a')
        ? 'A'
        : btn.classList.contains('dept-b')
          ? 'B'
          : btn.classList.contains('dept-c')
            ? 'C'
            : 'D';
      currentLeftChatModel = `dept-${id}`;
      updateActiveUI('left');
    });
  });

  document.querySelectorAll('.model-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
      const modelName = btn.dataset.model;
      currentRightChatModel = modelName;
      updateActiveUI('right');
      addMessage(
        rightChatLog,
        'Система',
        `Модель ${modelName} выбрана для диалога.`,
      );
    });
  });

  document.querySelectorAll('.mention-content a').forEach((link) => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const role = link.dataset.role;
      const isCeo = link
        .closest('.mention-menu')
        .querySelector('.mention-btn')
        .textContent.includes('СЕО');
      if (isCeo) {
        currentRightChatModel = role;
        updateActiveUI('right');
        addMessage(
          rightChatLog,
          'Система',
          `Модель ${role} выбрана из меню СЕО.`,
        );
      } else {
        currentLeftChatModel = role;
        updateActiveUI('left');
        addMessage(leftChatLog, 'Система', `Роль ${role} выбрана из меню ШЕФ.`);
      }
    });
  });

  const modal = document.getElementById('soulModal');
  const closeModal = document.getElementById('closeModal');
  if (closeModal) closeModal.onclick = () => (modal.style.display = 'none');
  window.onclick = (e) => {
    if (e.target == modal) modal.style.display = 'none';
  };

  // Инициализация
  loadDynamicModelMapping();
  updateActiveUI('left');
  connectGeminiWS(); // Автоматическое подключение MCP
  updateGCBQueue();
  setInterval(updateGCBQueue, 5000);

  async function updateGCBQueue() {
    try {
      const response = await fetch('/api/gcb/queue');
      const queue = await response.json();
      const container = document.getElementById('gcbQueue');
      if (!container || !Array.isArray(queue)) return;
      if (queue.length === 0) {
        initDashboard();
        return;
      }
      container.innerHTML = queue
        .reverse()
        .map(
          (item) => `
        <div class="gcb-item">
          <span class="gcb-status status-${item.status}">${item.status}</span>
          <span class="gcb-cmd">> ${item.command}</span>
          ${item.status === 'pending' ? `<button class="exec-btn" onclick="executeGCB('${item.id}')">Run</button>` : ''}
        </div>`,
        )
        .join('');
    } catch (e) {}
  }

  window.executeGCB = async function (id) {
    try {
      await fetch(`/api/gcb/execute/${id}`, { method: 'POST' });
      updateGCBQueue();
    } catch (e) {}
  };
});
