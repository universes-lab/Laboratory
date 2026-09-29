нашего Самурая выставил так:
/settings	Значение	Почему
Default Approval Mode	default	Самурай не должен самовольно выполнять изменения
Enable Auto Update	OFF	Зафиксировали рабочую версию 0.61.0; обновляем сознательно
Enable Plan Mode	ON	Полезно для разведки/планирования
Plan Model Routing	OFF	Чтобы Самурай не менял сам модель, заданную нами через --model
Retry Fetch Errors	ON	нормальная защита от сетевых сбоев
Max Chat Model Attempts	10	оставить default
Enable Session Cleanup	ON	не захламлять C:\Users\VAL\.gemini
Keep chat history	90d	вместо слишком коротких 30 дней
Topic & Update Narration	ON	меньше болтовни, структурированные отчёты
Hide Tips	ON	они нам уже не нужны
Hide Context Summary	OFF	важно видеть, какой GEMINI.md реально подхватился
Hide Model Info	OFF	видеть активную модель
Hide Context Window Percentage	OFF	будем видеть расход контекста
Compact Tool Output	ON	оставить
Error Verbosity	full	Самураю нужна нормальная диагностика, а не спрятанные ошибки
Model	не задавать	модель задаём строкой запуска --model ...
Max Session Turns	-1	не обрезать искусственно сессию
Load Memory From Include Directories	OFF	важно: не тащить GEMINI.md из соседних проектов
Respect .gitignore	ON	оставить
Respect .geminiignore	ON	оставить
Recursive File Search	ON	оставить
Use Ripgrep	ON	быстрее поиск по проекту
Disable LLM Correction	ON	детерминированные edits: не угадал строку → ошибка, а не самодеятельность
Disable YOLO Mode	ON	соответствует нашей дисциплине Самурая
Folder Trust	ON	оставить
Environment Variable Redaction	ON	особенно поскольку GEMINI_API_KEY лежит в environment
Auto Configure Max Old Space Size	ON	оставить

Это всё реальные текущие настройки Gemini CLI; workspace-настройки, если появятся, перекрывают пользовательские. Gemini CLI
Особенно для нашей архитектуры я выделяю четыре:
Auto Update                  OFF
Plan Model Routing           OFF
Load Memory From Include...  OFF
Disable YOLO Mode            ON

Первое сохраняет стабильность версии, второе не позволяет незаметно перескакивать между моделями, третье защищает от смешения HONC/Laboratory/Dojo/остальных проектов, четвёрто закрепляет нашу модель «Самурай действует в пределах разрешения». Официально defaultApprovalMode=default требует подтверждения инструментальных действий, а YOLO можно отдельно запрещать настройкой безопасности. Gemini CLI


Vim Mode                                                                                                                                 true*  │
Enable Vim keybindings                                                                                                                          │
                                                                                                                                                │
Default Approval Mode                                                                                                                  Default  │
The default approval mode for tool execution. 'default' prompts for approval, 'auto_edit' auto-approves edit tools, and 'plan' is r…            │
                                                                                                                                                │
Enable Auto Update                                                                                                                      false*  │
Enable automatic updates.                                                                                                                       │
                                                                                                                                                │
Enable Terminal Notifications                                                                                                            false  │
Enable terminal run-event notifications for action-required prompts and session completion.                                                     │
                                                                                                                                                │
Terminal Notification Method                                                                                                              Auto  │
How to send terminal notifications.                                                                                                             │
                                                                                                                                                │
Enable Plan Mode                                                                                                                          true  │
Enable Plan Mode for read-only safety during planning.                                                                                          │
                                                                                                                                                │
Plan Directory                                                                                                                       undefined  │
The directory where planning artifacts are stored. If not specified, defaults to the system temporary directory. A custom directo…              │
                                                                                                                                                │
Plan Model Routing                                                                                                                      false*  │
Automatically switch between Pro and Flash models based on Plan Mode status. Uses Pro for the planning phase and Flash for the imple…           │
                                                                                                                                                │
Retry Fetch Errors                                                                                                                        true  │
Retry on "exception TypeError: fetch failed sending request" errors.                                                                            │
                                                                                                                                                │
Max Chat Model Attempts                                                                                                                     10  │
Maximum number of attempts for requests to the main chat model. Cannot exceed 10.                                                               │
                                                                                                                                                │
Debug Keystroke Logging                                                                                                                  false  │
Enable debug logging of keystrokes to the console.                                                                                              │
                                                                                                                                                │
Enable Session Cleanup                                                                                                                    true  │
Enable automatic session cleanup                                                                                                                │
                                                                                                                                                │
Keep chat history                                                                                                                         90d*  │
Automatically delete chats older than this time period (e.g., "30d", "7d", "24h", "1w")                                                         │
                                                                                                                                                │
Topic & Update Narration                                                                                                                  true  │
Enable the Topic & Update communication model for reduced chattiness and structured progress reporting.                                         │
                                                                                                                                                │
Log RAG Snippets                                                                                                                         false  │
Log full Code Customization (RAG) retrieved snippets to a local file for debugging.                                                             │
                                                                                                                                                │
Output Format                                                                                                                             Text  │
The format of the CLI output. Can be `text` or `json`.                                                                                          │

Auto Theme Switching                                                                                                                      true
Automatically switch between default light and dark themes based on terminal background color.

Terminal Background Polling Interval                                                                                                        60
Interval in seconds to poll the terminal background color.

Hide Window Title                                                                                                                        false
Hide the window title bar

Inline Thinking                                                                                                                            Off
Display model thinking inline: off or full.

Show Thoughts in Title                                                                                                                   false
Show Gemini CLI model thoughts in the terminal window title during the working phase

Dynamic Window Title                                                                                                                      true
Update the terminal window title with current status icons (Ready: ◇, Action Required: ✋, Working: ✦)

Show Home Directory Warning                                                                                                               true
Show a warning when running Gemini CLI in the home directory.

Show Compatibility Warnings                                                                                                               true
Show warnings about terminal or OS compatibility issues.

Hide Tips                                                                                                                                true*
Hide helpful tips in the UI

Escape Pasted @ Symbols                                                                                                                  false
When enabled, @ symbols in pasted text are escaped to prevent unintended @path expansion.

Show Shortcuts Hint                                                                                                                       true
Show the "? for shortcuts" hint above the input.

Compact Tool Output                                                                                                                       true
Display tool outputs (like directory listings and file reads) in a compact, structured format.

Hide Banner                                                                                                                              true*
Hide the application banner

Hide Context Summary                                                                                                                     false
Hide the context summary (GEMINI.md, MCP servers) above the input.

Hide CWD                                                                                                                                 false
Hide the current working directory in the footer.

Hide Sandbox Status                                                                                                                      false
Hide the sandbox status indicator in the footer.

Hide Model Info                                                                                                                          false
Hide the model name and context usage in the footer.

Hide Context Window Percentage                                                                                                          false*
Hides the context window usage percentage.

Hide Footer                                                                                                                              false
Hide the footer from the UI

Show Memory Usage                                                                                                                        false
Display memory usage information in the UI

Show Line Numbers                                                                                                                         true
Show line numbers in the chat.

Show Citations                                                                                                                           false
Show citations for generated text in the chat.

Show Model Info In Chat                                                                                                                  false
Show the model name in the chat for each model turn.

Show User Identity                                                                                                                        true
Show the signed-in user's identity (e.g. email) in the UI.

Use Alternate Screen Buffer                                                                                                              false
Use an alternate screen buffer for the UI, preserving shell history.

Render Process                                                                                                                            true
Enable Ink render process for the UI.

Terminal Buffer                                                                                                                          false
Use the new terminal buffer architecture for rendering.

Use Background Color                                                                                                                      true
Whether to use background colors in the UI.

Incremental Rendering                                                                                                                     true
Enable incremental rendering for the UI. This option will reduce flickering but may cause rendering artifacts. Only supported when use…

Show Spinner                                                                                                                              true
Show the spinner during operations.

Loading Phrases                                                                                                                            Off
What to show while the model is working: tips, witty comments, all, or off.

Error Verbosity                                                                                                                          Full*
Controls whether recoverable errors are hidden (low) or fully shown (full).

Screen Reader Mode                                                                                                                       false
Render output in plain-text to be more screen reader accessible

IDE Mode                                                                                                                                 false
Enable IDE integration mode.

Overage Strategy                                                                                                                 Ask each time
How to handle quota exhaustion when AI credits are available. 'ask' prompts each time, 'always' automatically uses credits, '…

Model                                                                                                                                        *
The Gemini model to use for conversations.

Max Session Turns                                                                                                                           -1
Maximum number of user/model/tool turns to keep in a session. -1 means unlimited.

Context Compression Threshold                                                                                                        0.5 (50%)
The fraction of context usage at which to trigger context compression (e.g. 0.2, 0.3).

Disable Loop Detection                                                                                                                   false
Disable automatic detection and prevention of infinite loops.

Skip Next Speaker Check                                                                                                                   true
Skip the next speaker check.

Confirm Sensitive Actions                                                                                                                false
Require manual confirmation for sensitive browser actions (e.g., fill_form, evaluate_script).

Block File Uploads                                                                                                                       false
Hard-block file upload requests from the browser agent.

Memory Discovery Max Dirs                                                                                                                  200
Maximum number of directories to search for memory.

Load Memory From Include Directories                                                                                                     false
Controls how /memory reload loads GEMINI.md files. When true, include directories are scanned; when false, only the current directory…

Respect .gitignore                                                                                                                        true
Respect .gitignore files when searching.

Respect .geminiignore                                                                                                                     true
Respect .geminiignore files when searching.

Enable Recursive File Search                                                                                                              true
Enable recursive file search functionality when completing @ references in the prompt.

Enable Fuzzy Search                                                                                                                       true
Enable fuzzy search when searching for files.

Custom Ignore File Paths
Additional ignore file paths to respect. These files take precedence over .geminiignore and .gitignore. Files earlier in the array take pr…

Sandbox Allowed Paths
List of additional paths that the sandbox is allowed to access.

Sandbox Network Access                                                                                                                   false
Whether the sandbox is allowed to access the network.

Enable Interactive Shell                                                                                                                  true
Use node-pty for an interactive shell experience. Fallback to child_process still applies.

Show Color                                                                                                                                true
Show color in shell output.

Use Ripgrep                                                                                                                               true
Use ripgrep for file content search instead of the fallback implementation. Provides faster search performance.

Tool Output Truncation Threshold                                                                                                         40000
Maximum characters to show when truncating large tool outputs. Set to 0 or negative to disable truncation.

Disable LLM Correction                                                                                                                    true
Disable LLM-based error correction for edit tools. When enabled, tools will fail immediately if exact string matches are not found, in…

Tool Sandboxing                                                                                                                          false
Tool-level sandboxing. Isolates individual tools instead of the entire CLI process.

Disable YOLO Mode                                                                                                                        true*
Disable YOLO mode, even if enabled by a flag.

Disable Always Allow                                                                                                                     false
Disable "Always allow" options in tool confirmation dialogs.

Allow Permanent Tool Approval                                                                                                            false
Enable the "Allow for all future sessions" option in tool confirmation dialogs.

Auto-add to Policy by Default                                                                                                            false
When enabled, the "Allow for all future sessions" option becomes the default choice for low-risk tools in trusted workspaces.

Blocks extensions from Git                                                                                                               false
Blocks installing and loading extensions from Git.

Extension Source Regex Allowlist
List of Regex patterns for allowed extensions. If nonempty, only extensions that match the patterns in this list are allowed. Overrides th…

Folder Trust                                                                                                                              true
Setting to track whether Folder trust is enabled.

Enable Environment Variable Redaction                                                                                                    true*
Enable redaction of environment variables that may contain secrets.

Enable Context-Aware Security                                                                                                            false
Enable the context-aware security checker. This feature uses an LLM to dynamically generate and enforce security policies for tool us…

Auto Configure Max Old Space Size                                                                                                         true
Automatically configure Node.js memory limits. Note: Because memory is allocated during the initial process boot, this setting is only…

Ignore Local .env                                                                                                                        false
Whether to ignore generic .env files in the project directory.

Gemma Models                                                                                                                              true
Enable access to Gemma 4 models via Gemini API.

Voice Mode                                                                                                                               false
Enable experimental voice dictation and commands (/voice, /voice model).

Voice Activation Mode                                                                                                Push-To-Talk (Hold Space)
How to trigger voice recording with the Space key.

Voice Transcription Backend                                                                                            Gemini Live API (Cloud)
The backend to use for voice transcription. Note: When using the Gemini Live backend, voice recordings are sent to …

Whisper Model                                                                                                    Base (EN) - Balanced (~142MB)
The Whisper model to use for local transcription.

Voice Stop Grace Period (ms)                                                                                                              4000
How long to wait for final transcription after stopping recording.

Enable Git Worktrees                                                                                                                     false
Enable automated Git worktree management for parallel work.

Use OSC 52 Paste                                                                                                                         false
Use OSC 52 for pasting. This may be more robust than the default system when using remote terminal sessions (if your terminal is conf…

Use OSC 52 Copy                                                                                                                          false
Use OSC 52 for copying. This may be more robust than the default system when using remote terminal sessions (if your terminal is conf…

Model Steering                                                                                                                           false
Enable model steering (user hints) to guide the model during tool execution.

Direct Web Fetch                                                                                                                         false
Enable web fetch behavior that bypasses LLM summarization.

Enable Gemma Model Router                                                                                                                false
Enable the Gemma Model Router (experimental). Requires a local endpoint serving Gemma via the Gemini API using LiteRT-LM shim.

Auto-start LiteRT Server                                                                                                                 false
Automatically start the LiteRT-LM server when Gemini CLI starts and the Gemma router is enabled.

Auto Memory                                                                                                                              false
Automatically extract memory patches and skills from past sessions in the background. Every change is written as a unified diff `.pat…

Use the generalist profile to manage agent contexts.                                                                                     false
Suitable for general coding and software development tasks.

Enable Context Management                                                                                                                false
Enable logic for context management.

Enable Agent Skills                                                                                                                       true
Enable Agent Skills.

Enable Hooks                                                                                                                              true
Canonical toggle for the hooks system. When disabled, no hooks will be executed.

Hook Notifications                                                                                                                        true
Show visual indicators when hooks are executing.

---
несколько пунктов я бы подправил.
1. Vim Mode = true*
Если ты специально Vim-клавиши не используешь — ставь:
Vim Mode = false

Иначе можно случайно попасть в командный режим и потом гадать, почему ввод ведёт себя странно.
2. Confirm Sensitive Actions = false
Для нашей дисциплины Самурая лучше:
Confirm Sensitive Actions = true

Это относится прежде всего к браузерным действиям вроде заполнения форм, выполнения script/evaluate и тому подобного. Нам лишнее подтверждение там полезнее, чем автономия.
3. Disable Always Allow = false
Я бы поставил:
Disable Always Allow = true

Тогда Самурай не сможет получить широкое «разрешить всё такое дальше» одним неосторожным выбором. Это хорошо согласуется с нашим принципом: разрешение относится к конкретной операции, а не превращается в бессрочный пропуск.
При этом:
Allow Permanent Tool Approval = false
Auto-add to Policy by Default = false

уже выставлены правильно.
4. Plan Directory = undefined
Вот это интересный момент с учётом нашей борьбы за C:. При undefined планы пишутся в системный %TEMP%, то есть обычно на C:.
Я бы задал:
E:\Samurai_Software\Gemini\plans

или ещё аккуратнее:
E:\Samurai_Software\gemini-data\plans
