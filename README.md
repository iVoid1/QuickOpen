# QuickOpen ⚡

A versatile asynchronous keyboard shortcut manager with configurable actions, implemented in Python.

## 🌟 Features

- Asynchronous keyboard event handling
- Cofigurable hotkey-to-action mapping
- JSON-based configuration management
- Background operation with graceful shutdown
- Comprehensive logging system
- Type-safe implementation

## 🚀 Quick Start

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Run application
python quickopen/main_app.py
```

## 📁 Project Structure

```
QuickOpen/
├── python/
│   ├── quickopen/
│   │   ├── module/
│   │   │   ├── config.py
│   │   │   └── actions.json
│   │   ├── listener.py
│   │   ├── action_handler.py
│   │   └── main_app.py
|   ├── quickopen-gui/
|   | 
│   └── requirements.txt
└── README.md
```

## 🛠️ Development Setup

### Prerequisites

- Python 3.8+
- Git

### Required Packages

```txt
keyboard>=0.13.5
asyncio
typing
logging
pathlib
```

## 💡 Usage Examples

### Configuration Format

```json
{
    "ctrl shift n": "code .",
    "ctrl alt b": "chrome.exe",
    "alt t": "wt.exe"
}
```

### Code Example

```python

```

## 🔄 Key Components

### MainApp

- Manages application lifecycle
- Handles async task coordination
- Provides graceful shutdown

### Listener

- Captures keyboard events asynchronously
- Manages hotkey combinations
- Implements customizable key ordering

### ActionHandler

- Executes commands based on hotkeys
- Manages action configuration
- Provides async operation support

### Config

- Handles JSON configuration
- Supports both dict and list configurations
- Implements auto-save functionality

## 🤝 Contributing

1. Fork repository
2. Create feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add YourFeature'`)
4. Push to branch (`git push origin feature/YourFeature`)
5. Open Pull Request

## 🐛 Issue Tracking

Report bugs and request features through:

- [GitHub Issues](https://github.com/iVoid1/QuickOpen/issues)

## 📫 Contact

- GitHub: [@iVoid1](https://github.com/iVoid1)
- Email: yousef.a.a.mutawa@gmail.com

---

Made with ❤️ by iVoid1
