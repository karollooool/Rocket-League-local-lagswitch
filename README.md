# 🚀 Rocket League Lag Switch

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Windows](https://img.shields.io/badge/OS-Windows-blue.svg)](https://www.microsoft.com/windows)
[![License](https://img.shields.io/badge/License-Educational-yellow.svg)](#disclaimer)

A Windows-based network traffic controller for Rocket League using firewall rules and mouse input detection.

## ⚠️ **IMPORTANT DISCLAIMER**

> **WARNING**:  This tool is intended for **EDUCATIONAL AND RESEARCH PURPOSES ONLY**. 
> 
> - Using lag switches in online games is considered **CHEATING**
> - Violates Rocket League's Terms of Service
> - May result in permanent account bans
> - Could negatively impact other players' gaming experience
> 
> **USE AT YOUR OWN RISK** - The author is not responsible for any consequences. 

## 🎯 Features

- **🖱️ Mouse Control**: Toggle with side mouse button (X2)
- **🔥 Firewall Integration**: Uses Windows Advanced Firewall
- **🎮 Process Detection**: Automatically finds Rocket League process
- **🛡️ Admin Protection**: Requires administrator privileges
- **🧹 Auto Cleanup**: Removes firewall rules on exit
- **📊 Real-time Status**: Console feedback for all operations

## 📋 Requirements

### System Requirements
- **OS**: Windows 10/11
- **Python**: 3.7 or higher
- **Privileges**: Administrator rights required

### Dependencies
```bash
pip install psutil mouse
```

## 🚀 Installation

1. **Clone or download** the script: 
   ```bash
   git clone https://github.com/yourusername/rocket-league-lagswitch.git
   cd rocket-league-lagswitch
   ```

2. **Install dependencies**:
   ```bash
   pip install psutil mouse
   ```

3. **Run as Administrator**:
   - Right-click Command Prompt → "Run as administrator"
   - Navigate to script directory
   - Execute: `python karollol_lagswitch. py`

## 🎮 Usage

### Basic Operation

1. **Launch** the script with administrator privileges
2. **Start** Rocket League
3. **Press** your mouse side button (X2) to toggle lag switch
4. **Monitor** console output for status updates
5. **Exit** with `Ctrl+C` to cleanup

### Controls

| Input | Action |
|-------|--------|
| `Mouse Side Button (X2)` | Toggle lag switch ON/OFF |
| `Ctrl+C` | Exit and cleanup |

### Console Output
```
============================================================
  Rocket League Lag Switch - Security Research Tool
  Based on Leaf Lag Switch by SquareszLeaf
============================================================

[INFO] Keybind:  Mouse Side Button (X2)
[INFO] Target: RocketLeague. exe
[INFO] Status: Ready

Press your mouse side button to toggle lag switch ON/OFF
Press CTRL+C to exit

[LAG SWITCH] ENABLED - RocketLeague.exe outbound traffic BLOCKED
[LAG SWITCH] DISABLED - Normal network restored
```

## ⚙️ Configuration

### Customizable Settings

```python
# In karollol_lagswitch. py
FIREWALL_RULE_NAME = "RocketLeague_Block"      # Firewall rule name
TOGGLE_MOUSE_BUTTON = "x2"                     # Mouse button (x1, x2, etc.)
TARGET_PROCESS_NAME = "RocketLeague. exe"       # Target process
DEFAULT_RL_PATH = r"C:\Program Files\Epic Games\rocketleague\Binaries\Win64\RocketLeague.exe"
```

## 🔧 Technical Details

### How It Works

1. **Process Detection**: Scans running processes for `RocketLeague.exe`
2. **Firewall Rules**:  Creates/deletes Windows Firewall rules to block outbound traffic
3. **Mouse Hooks**: Uses global mouse hook to detect side button presses
4. **Real-time Toggle**: Instantly enables/disables network blocking

### Firewall Commands
```cmd
# Block traffic
netsh advfirewall firewall add rule name=RocketLeague_Block dir=out action=block program=<RL_PATH>

# Restore traffic
netsh advfirewall firewall delete rule name=RocketLeague_Block
```

## 🛠️ Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| **"Access Denied"** | Run as Administrator |
| **Mouse not detected** | Check if mouse has side buttons |
| **Process not found** | Start Rocket League first |
| **Firewall errors** | Check Windows Firewall service |

### Debug Mode
Enable debug output by modifying the script:
```python
DEBUG = True  # Add this at the top of the file
```

## 📁 File Structure

```
karollol_lagswitch/
├── karollol_lagswitch.py    # Main script
├── README. md                # This file
└── requirements.txt         # Python dependencies
```

## 🤝 Contributing

This is an educational project. If you want to contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📜 License & Ethics

### Educational Use Only
This software is provided for: 
- **Network research**
- **Educational purposes**
- **Understanding firewall manipulation**
- **Security testing**

### Prohibited Uses
- **Online gaming cheating**
- **Competitive advantage**
- **Terms of Service violations**
- **Harm to other players**

## 🙏 Credits

- **Original Concept**:  Leaf Lag Switch by SquareszLeaf
- **Author**: karollooool
- **Libraries**: psutil, mouse, ctypes

---

<div align="center">

**⚡ Remember: With great power comes great responsibility ⚡**

*Use this tool ethically and responsibly*

</div>
