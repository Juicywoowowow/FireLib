#!/usr/bin/env python
"""
Firelib Installer
Detects Python version, checks dependencies, and installs Firelib
"""
import os
import sys
import subprocess
import shutil

class FirelibInstaller:
    def __init__(self):
        self.python_cmd = None
        self.python_version = None
        self.prefix = os.environ.get('PREFIX', '/data/data/com.termux/files/usr')
        self.home = os.path.expanduser('~')
        self.firelib_home = os.path.join(self.home, '.firelib')
        
    def detect_python(self):
        """Detect available Python interpreter"""
        print("[*] Detecting Python...")
        for cmd in ['python3', 'python', 'python2']:
            if shutil.which(cmd):
                try:
                    result = subprocess.run([cmd, '--version'], 
                                          capture_output=True, text=True)
                    version_str = result.stdout + result.stderr
                    self.python_cmd = cmd
                    self.python_version = version_str.strip()
                    print("[+] Found: " + self.python_version)
                    return True
                except:
                    continue
        print("[!] No Python found. Install with: pkg install python")
        return False
    
    def check_termux(self):
        """Verify we're running in Termux"""
        print("[*] Checking Termux environment...")
        if not os.path.exists(self.prefix):
            print("[!] Not running in Termux!")
            return False
        print("[+] Termux detected: " + self.prefix)
        return True
    
    def install_dependencies(self):
        """Install required system packages"""
        print("[*] Checking dependencies...")
        required = ['clang', 'make', 'binutils']
        missing = []
        
        for pkg in required:
            if not shutil.which(pkg):
                missing.append(pkg)
        
        if missing:
            print("[*] Installing missing packages: " + ', '.join(missing))
            cmd = ['pkg', 'install', '-y'] + missing
            subprocess.run(cmd)
        else:
            print("[+] All dependencies satisfied")
    
    def create_directories(self):
        """Create necessary directories"""
        print("[*] Creating directories...")
        dirs = [
            self.firelib_home,
            os.path.join(self.firelib_home, 'config'),
            os.path.join(self.firelib_home, 'data'),
            os.path.join(self.firelib_home, 'logs')
        ]
        for d in dirs:
            if not os.path.exists(d):
                os.makedirs(d)
        print("[+] Created " + self.firelib_home)
    
    def compile_core(self):
        """Compile C/C++ components"""
        print("[*] Compiling core components...")
        if os.path.exists('Makefile'):
            result = subprocess.run(['make', 'clean'])
            result = subprocess.run(['make'])
            if result.returncode == 0:
                print("[+] Compilation successful")
                return True
            else:
                print("[!] Compilation failed")
                return False
        else:
            print("[*] No Makefile found, skipping compilation")
            return True
    
    def install_binaries(self):
        """Install binaries to PREFIX/bin"""
        print("[*] Installing binaries...")
        bin_dir = os.path.join(self.prefix, 'bin')
        src_bin = 'bin'
        
        if not os.path.exists(src_bin):
            print("[!] No bin directory found")
            return False
        
        installed = 0
        for item in os.listdir(src_bin):
            src = os.path.join(src_bin, item)
            dst = os.path.join(bin_dir, item)
            if os.path.isfile(src):
                shutil.copy2(src, dst)
                os.chmod(dst, 0o755)
                installed += 1
        
        print("[+] Installed " + str(installed) + " commands")
        return True
    
    def install_python_package(self):
        """Install Python package"""
        print("[*] Installing Python package...")
        if os.path.exists('src/python/firelib'):
            cmd = [self.python_cmd, '-m', 'pip', 'install', '-e', '.']
            result = subprocess.run(cmd)
            if result.returncode == 0:
                print("[+] Python package installed")
                return True
        return True
    
    def run(self):
        """Run the installation"""
        print("=" * 50)
        print("Firelib Installer")
        print("=" * 50)
        
        if not self.check_termux():
            sys.exit(1)
        
        if not self.detect_python():
            sys.exit(1)
        
        self.install_dependencies()
        self.create_directories()
        self.compile_core()
        self.install_binaries()
        self.install_python_package()
        
        print("\n" + "=" * 50)
        print("[+] Firelib installed successfully!")
        print("=" * 50)
        print("\nTry: fire-serve --help")

if __name__ == '__main__':
    installer = FirelibInstaller()
    installer.run()
