# QuickOpen ⚡

A versatile tool for managing keyboard shortcuts across different platforms, implementation in Python.

## 🌟 Implementation

- Global keyboard event capture
- Custom action mapping
- JSON configuration
- Background operation

## 🚀 Quick Start

### Python Implementation

```bash
# Install dependencies
pip install -r requirements.txt

# Run application
python main.py
```

## 📁 Project Structure

```
QucikOpen/
├── python/
│   ├── quickopen/
│   │   ├── module/
│   │   └── scripts/
│   ├── test.py
│   └── requirements.txt
└── docs/
    └── Python.md
```

## 🛠️ Development Setup

### Prerequisites

- Python 3.8+
- Git

### Required Packages

#### Python

```txt
keyboard>=0.13.5
pynput>=1.7.6
```

## 💡 Usage Examples

### Python Configuration

```json
{
    "Ctrl+Alt+N":
    {
        "id": 1,
        "name": "Open vscode",
        "command": "Code.exe"
    },

    "Ctrl+Shift+B":
    {
        "id": 2,
        "name": "Open Browser",
        "command": "Arc.exe"
    }
}
```

## 🔄 Features

### Common Features

- Global shortcut detection
- Custom action mapping
- Configuration persistence
- Background operation

## 🤝 Contributing

1. Fork repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📚 Documentation

[Python Documentation](docs/Python.md)

## 🐛 Issue Tracking

Report bugs and request features through:

- [GitHub Issues](https://github.com/iVoid1/Shortcut-Manager/issues)

## 📫 Contact

- GitHub: [@iVoid1](https://github.com/iVoid1)
- Email: yousef.a.a.mutawa@gmail.com

---

Made with by iVoid1
