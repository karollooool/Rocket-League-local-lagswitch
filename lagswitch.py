import ctypes as ct
import mouse
import psutil
import sys
import time

RL_PROCESS_NAME = "RocketLeague.exe"
MOUSE_BUTTON = "x2"  # Side button 2 (VK_XBUTTON2)

# Windows API constants
PROCESS_SUSPEND_RESUME = 0x0800
THREAD_SUSPEND_RESUME = 0x0002

# Load kernel32.dll
kernel32 = ct.windll.kernel32

class ProcessLagSwitch:
    """
    Lag switch that works by SUSPENDING the game process.
    This is the most reliable method - when suspended, the game literally cannot send data.
    """
    def __init__(self):
        self.process = None
        self.suspended = False
        self.keybind_handler = None
        
        if not self.is_admin():
            self.show_message('This tool requires administrator privileges!')
            sys.exit(1)
        
        print("\n" + "="*60)
        print("  Rocket League Process Lag Switch")
        print("  Confuse niggas with lags")
        print("="*60)
        print(f"\n[INFO] Keybind: Mouse Side Button (X2)")
        print("[INFO] Searching for Rocket League process...")
        
        self.find_process()
        self.setup_keybind()
        
        print("\n READY! Press your mouse side button to freeze/unfreeze the game")
        print("Press CTRL+C to exit\n")
    
    def find_process(self):
        """Find the Rocket League process"""
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == RL_PROCESS_NAME:
                self.process = proc
                print(f"[SUCCESS] Found {RL_PROCESS_NAME} (PID: {proc.pid})")
                return True
        
        print(f"[ERROR] {RL_PROCESS_NAME} is not running!")
        print("Please start Rocket League and try again.")
        sys.exit(1)
    
    def suspend_process(self):
        """Suspend the Rocket League process (freeze it)"""
        try:
            if not self.process or not self.process.is_running():
                print("[ERROR] Process not found, searching again...")
                self.find_process()
            
            # Suspend all threads in the process
            for thread in self.process.threads():
                handle = kernel32.OpenThread(THREAD_SUSPEND_RESUME, False, thread.id)
                if handle:
                    kernel32.SuspendThread(handle)
                    kernel32.CloseHandle(handle)
            
            self.suspended = True
            print("\n [LAG SWITCH] ENABLED - Process FROZEN")
            print("[INFO] Game is completely paused - no data can be sent!")
            print("[WARNING] Don't keep it frozen too long or you'll timeout\n")
            
        except Exception as e:
            print(f"[ERROR] Failed to suspend: {e}")
    
    def resume_process(self):
        """Resume the Rocket League process (unfreeze it)"""
        try:
            if not self.process or not self.process.is_running():
                print("[ERROR] Process not found!")
                return
            
            # Resume all threads in the process
            for thread in self.process.threads():
                handle = kernel32.OpenThread(THREAD_SUSPEND_RESUME, False, thread.id)
                if handle:
                    kernel32.ResumeThread(handle)
                    kernel32.CloseHandle(handle)
            
            self.suspended = False
            print("\n [LAG SWITCH] DISABLED - Process RESUMED")
            print("[INFO] Game is running normally again\n")
            
        except Exception as e:
            print(f"[ERROR] Failed to resume: {e}")
    
    def toggle(self):
        """Toggle between suspended and resumed"""
        if self.suspended:
            self.resume_process()
        else:
            self.suspend_process()
    
    def setup_keybind(self):
        """Setup the mouse side button"""
        mouse.on_button(self.toggle, buttons=(MOUSE_BUTTON,), types=(mouse.DOWN,))
    
    def is_admin(self):
        """Check if running with administrator privileges"""
        try:
            return bool(ct.windll.shell32.IsUserAnAdmin())
        except:
            return False
    
    def show_message(self, msg):
        """Show Windows message box"""
        ct.windll.user32.MessageBoxW(0, msg, 'RL Lag Switch', 0)
    
    def cleanup(self):
        """Make sure process is resumed on exit"""
        if self.suspended:
            print("\n[CLEANUP] Resuming process...")
            self.resume_process()
        # Unhook all mouse events
        mouse.unhook_all()
    
    def run(self):
        """Main loop"""
        try:
            # Keep running indefinitely
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("\n[EXIT] Shutting down...")
            self.cleanup()

if __name__ == '__main__':
    try:
        app = ProcessLagSwitch()
        app.run()
    except Exception as e:
        print(f"\n[FATAL ERROR] {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
