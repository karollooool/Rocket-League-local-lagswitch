# ⏸️ Rocket League Process Lag Switch

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Windows](https://img.shields.io/badge/OS-Windows-blue.svg)](https://www.microsoft.com/windows)
[![Method](https://img.shields.io/badge/Method-Process%20Suspension-orange.svg)](#how-it-works)

A Windows-based lag switch using **process suspension** - the most reliable method for freezing game network communication.

## ⚠️ **CRITICAL WARNING**

> **DANGER**:  This tool is for **EDUCATIONAL AND RESEARCH PURPOSES ONLY**
> 
> - Using lag switches in online games is **CHEATING** and **UNETHICAL**
> - Violates Rocket League's Terms of Service 
> - **WILL RESULT IN PERMANENT BANS** if detected
> - Ruins the gaming experience for other players
> - May violate local laws regarding unfair gaming practices
> 
> **YOU HAVE BEEN WARNED** - Use at your own risk.  Author assumes no responsibility. 

## 🔬 **Technical Overview**

### Process Suspension Method
This lag switch works by **completely freezing** the Rocket League process using Windows API calls: 

```python
# Suspend all game threads - COMPLETE FREEZE
for thread in self.process.threads():
    kernel32.SuspendThread(handle)    # Game literally cannot run
    
# Resume all game threads - BACK TO NORMAL  
for thread in self.process. threads():
    kernel32.ResumeThread(handle)     # Game continues normally
```

## 📋 **System Requirements**

### Hardware & OS
- **OS**: Windows 10/11 (64-bit recommended)
- **RAM**: 4GB+ (for Rocket League + this tool)
- **Mouse**: Side buttons required (X1/X2)
- **Privileges**: Administrator access **MANDATORY**

### Dependencies
```bash
pip install psutil mouse
```

## 🎯 **Installation**

1. **Download** the script: 
   ```bash
   git clone 
   ```

2. **Install dependencies**:
   ```bash
   pip install psutil mouse
   ```

3. **Run as Administrator** (REQUIRED):
   ```cmd
   # Right-click Command Prompt → "Run as administrator"
   cd /path/to/script
   python rl_lagswitch_suspend.py
   ```

## 🎮 **Usage Guide**

### Step-by-Step Operation

1. **Start Rocket League** first
2. **Launch script** with admin privileges  
3. **Wait** for process detection
4. **Press** mouse side button to toggle freeze/unfreeze
5. **Exit** with `Ctrl+C` when done

### Console Output Example
```
============================================================
  Rocket League Process Lag Switch
  METHOD: Process Suspension (Most Reliable)
============================================================

[INFO] Keybind: Mouse Side Button (X2)
[INFO] Searching for Rocket League process...
[SUCCESS] Found RocketLeague.exe (PID: 12345)

✅ READY!  Press your mouse side button to freeze/unfreeze the game
Press CTRL+C to exit

🔴 [LAG SWITCH] ENABLED - Process FROZEN
[INFO] Game is completely paused - no data can be sent! 
[WARNING] Don't keep it frozen too long or you'll timeout

🟢 [LAG SWITCH] DISABLED - Process RESUMED  
[INFO] Game is running normally again
```

## ⚙️ **Configuration**

### Customizable Settings
```python
# Target process name
RL_PROCESS_NAME = "RocketLeague.exe"

# Mouse button (x1, x2, middle, etc.)
MOUSE_BUTTON = "x2"  # Side button 2

# Windows API permissions
THREAD_SUSPEND_RESUME = 0x0002
```

### Alternative Mouse Buttons
| Button Code | Description |
|-------------|-------------|
| `"x1"` | Side button 1 (back) |
| `"x2"` | Side button 2 (forward) |
| `"middle"` | Mouse wheel click |
| `"right"` | Right mouse button |

## 🔧 **Technical Deep Dive**

### Windows API Calls Used
```python
# Open thread handle with suspend/resume permissions
handle = kernel32.OpenThread(THREAD_SUSPEND_RESUME, False, thread_id)

# Suspend thread (freeze execution)
kernel32.SuspendThread(handle)

# Resume thread (continue execution)  
kernel32.ResumeThread(handle)

# Close thread handle (cleanup)
kernel32.CloseHandle(handle)
```

### Process vs Firewall Methods

| Aspect | Process Suspension | Firewall Blocking |
|--------|-------------------|-------------------|
| **Reliability** | 🟢 100% | 🟡 95% |
| **Speed** | 🟢 Instant | 🟡 ~100ms |
| **Detection Risk** | 🟢 Very Low | 🟡 Medium |
| **Resource Usage** | 🟢 Minimal | 🟡 Moderate |
| **Cleanup** | 🟢 Automatic | 🟡 Manual rules |

## 🛠️ **Troubleshooting**

### Common Issues

| Problem | Cause | Solution |
|---------|-------|----------|
| **"Access Denied"** | Not admin | Run as Administrator |
| **"Process not found"** | RL not running | Start Rocket League first |
| **Mouse not responding** | No side buttons | Use mouse with X1/X2 buttons |
| **Freeze not working** | API permissions | Check Windows version compatibility |
| **Game won't resume** | Handle leak | Restart script, then game |

### Debug Mode
Add debug output to track thread operations:
```python
def suspend_process(self):
    print(f"[DEBUG] Found {len(self.process.threads())} threads")
    for thread in self.process.threads():
        print(f"[DEBUG] Suspending thread {thread.id}")
        # ...  suspend logic
```

### Recovery Commands
If game gets stuck frozen:
```cmd
# Kill Rocket League process  
taskkill /f /im RocketLeague.exe

# Or restart from Task Manager
Ctrl+Shift+Esc → Find RocketLeague.exe → End Task
```

## 🚨 **Safety & Ethics**

### Recommended Usage
- **✅ Single-player testing only**
- **✅ Network research purposes**  
- **✅ Understanding Windows APIs**
- **✅ Educational demonstrations**

### Prohibited Usage
- **❌ Online competitive matches**
- **❌ Ranked gameplay**
- **❌ Tournaments or leagues**
- **❌ Any multiplayer scenarios**
- **❌ Streaming/recording for content**

### Detection Risks
```
Low Risk:     Process suspension appears normal to system
Medium Risk:  Unusual network patterns may be logged
High Risk:   Repeated pattern usage in online matches
```

## 📁 **File Structure**

```
rl-lagswitch-suspend/
├── rl_lagswitch_suspend.py    # Main script
├── README.md                  # Documentation  
├── requirements.txt           # Dependencies
└── LICENSE                    # Usage terms
```

## 🤝 **Contributing**

Ccontributions should focus on:
- 📚 Educational improvements
- 🔧 Code optimization
- 📖 Documentation updates
- 🛡️ Safety enhancements

**NOT acceptable**:
- Features for competitive advantage
- Anti-detection mechanisms
- Automation for repeated use

## 📜 **License**

This software is proprietary with restrictive terms. See [LICENSE](LICENSE) file. 

**TL;DR**: Educational use only - no distribution, modification, or commercial use. 

## ⚖️ **Legal Disclaimer**

```
THIS SOFTWARE IS PROVIDED FOR EDUCATIONAL PURPOSES ONLY.
THE AUTHOR DISCLAIMS ALL LIABILITY FOR MISUSE. 
USERS ARE RESPONSIBLE FOR COMPLIANCE WITH: 
- Game Terms of Service
- Local and international laws  
- Ethical gaming standards
- Platform-specific rules
```

---

<div align="center">

**🎮 Game Responsibly - Research Ethically 🎮**

*Understanding technology ≠ Abusing technology*

[![Educational](https://img.shields.io/badge/Purpose-Educational-green.svg)](https://github.com/yourusername/rl-lagswitch-suspend)

</div>
