Installation
---

---

Install prerequisites, this may not be comprehensive:

```
sudo apt-get install libssl-dev libffi-dev
```

Add/edit `/etc/pip.conf` file, adding the following section:

```
[global]
timeout = 60
extra-index-url = https://developer.naz.edu/pypi/simple/
```

Run the following command:

```
sudo pip3 install nazops
```

Usage
---

Type nazops in the command line after installation and use the help there.