# Shortcut Manager 🎮

A versatile tool for managing keyboard shortcuts across different platforms, with implementations in both Python and C#.

## 🌟 Implementations

### Python Version

- Global keyboard event capture
- Custom action mapping
- JSON configuration
- Background operation

### C# Version (Windows Forms)

- System-wide shortcut detection
- Modern Windows Forms UI
- System tray integration
- Persistent settings
- Action automation

## 🚀 Quick Start

### Python Implementation

```bash
# Install dependencies
pip install -r requirements.txt

# Run application
python shortcutmanager.py
```

### C# Implementation

```powershell
# Build solution
dotnet build

# Run application
dotnet run
```

## 📁 Project Structure

```
Shortcut-Manager/
├── python/
│   ├── shortcutmanager/
│   │   ├── module/
│   │   └── scripts/
│   ├── tests/
│   └── requirements.txt
│
├── csharp/
│   ├── Shortcut-ManagerWFA/
|   |
|   |── Shortcut-ManagerWPF/
|   |
│   └── Tests/
│
└── docs/
    ├── Python.md
    └── CSharp.md
```

## 🛠️ Development Setup

### Prerequisites

- Python 3.8+
- .NET 6.0+
- Visual Studio 2022 or VS Code
- Git

### Required Packages

#### Python

```txt
keyboard>=0.13.5
pynput>=1.7.6
```

#### C# (NuGet)

```xml
<PackageReference Include="InputSimulator" Version="1.0.4" />
<PackageReference Include="Newtonsoft.Json" Version="13.0.3" />
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

### C# Implementation

```csharp
shortcutManager.RegisterShortcut(
    Keys.Control | Keys.Alt | Keys.N,
    () => Process.Start("notepad.exe")
);
```

## 🔄 Features

### Common Features

- Global shortcut detection
- Custom action mapping
- Configuration persistence
- Background operation

### Platform-Specific Features

- Python: Cross-platform support
- C#: Windows integration
- System tray operations (C#)
- GUI interface (C#)

## 🤝 Contributing

1. Fork repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📚 Documentation

- [Python Documentation](docs/Python.md)
- [C# Documentation](docs/CSharp.md)
- [API Reference](docs/API.md)
- [Contributing Guidelines](CONTRIBUTING.md)

## 🐛 Issue Tracking

Report bugs and request features through:

- [GitHub Issues](https://github.com/iVoid1/Shortcut-Manager/issues)

## 📫 Contact

- GitHub: [@iVoid1](https://github.com/iVoid1)
- Email: yousef.a.a.mutawa@gmail.com

---

Made with ❤️ by [iVoid1]
