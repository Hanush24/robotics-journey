## 🎯 Goal:
Be fluent in navigating the Linux ZSH terminal, handling permissions, and scripting like a pro.

---

## 📒 linux_notes_day3.md – My Day 3 Linux Learning Journey

### ✅ Topics Covered:
- File and network searching (find, locate, grep)
- Understanding file permissions (chmod, chown)
- Making and using aliases
- Writing and running ZSH shell scripts
- System monitoring with top, htop, df, du
- Networking tools (ping, ifconfig, netstat)
- Concept of port numbers, broadcasting, and local IPs

---

### 🧠 Key Commands Practiced:
```zsh
find ~ -name "*.py"                  # Find files
locate myfile.txt                    # Locate files (after installing plocate)
grep "def" *.py                     # Search inside files
ls -l                                # Check permissions
chmod +x filename                    # Make script executable
sudo chown hanush filename          # Change file ownership
alias gs='git status'               # Temporary alias
echo "alias gs='git status'" >> ~/.zshrc && source ~/.zshrc  # Permanent alias
nano hello_robot.sh                 # Made a shell script
./hello_robot.sh                    # Ran the script
htop, df -h, du -sh ~/*             # System resource monitoring
ping google.com                     # Check internet
ifconfig                             # IP and network info
netstat -tulnp                       # Check open ports
```

---

### ⚠️ Problems Faced & Fixes:
- ❌ Tried `sudo updatedb` → **error**: “command not found”
  - ✅ Fixed it by installing `plocate`: `sudo apt install plocate`
- ❌ Script only ran in the folder it was created
  - ✅ Solved by adding script path to `~/.zshrc` as alias:
    ```zsh
    alias shutdownme='~/scripts/shutdown_now.sh'
    ```
- ❌ Confused by `broadcast` and `netstat`
  - ✅ Learned that broadcast can send messages to all devices on the same LAN (like a raw version of Airdrop)
- ❓ Asked: “Is Wi-Fi considered LAN?”
  - ✅ Yes, it is. Wi-Fi is a wireless type of LAN.
- 🤔 Didn’t understand ports initially
  - ✅ Learned that ports are like door numbers inside your system, helping apps communicate without clashing.

---

### 🚀 Mini Projects I Built Today:
- Created a **shutdown script** that powers off the system with a command
- Learned how to **broadcast messages over local Wi-Fi** using `nc`
- Started thinking about building my own **LAN-based chat app**

---

### 🧠 Key Concepts Burned Into My Brain:
- Every network service uses a port → IP + port = full address
- Scripts can be automated using aliases or placing them in `~/.local/bin`
- Wi-Fi broadcast address (`192.168.1.255`) can send messages to all connected devices
- Tools like `netstat` and `ifconfig` give deep insights about system connections

---

### ❤️ Final Thoughts:
Today was full hacker mode 😎. I struggled, Googled, asked ChatGPT like 50 times, and **finally cracked Day 3** of Linux. 

Felt like a robot when trying to understand `port`, `broadcast`, and `netstat`, but now it all feels like real-world superpowers.



