#!/data/data/com.termux/files/usr/bin/bash
case "$1" in
  bill) python3 ~/GODMODE/core.py --bill "$2" ;;
  whatsapp) python3 ~/GODMODE/core.py --whatsapp "$2" ;;
  map) python3 ~/GODMODE/core.py --map ;;
  *) python3 ~/GODMODE/core.py --$1 ;;
esac
