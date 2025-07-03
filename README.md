# Inkscape Metaball Extension

This Inkscape extension allows you to create dynamic and organic-looking metaball shapes directly within Inkscape.

![App Screenshot](https://inkscape.gitlab.io/extensions/documentation/_images/color.png)

## Table of contents

- [Installation](#installation)
- [Usage](#usage)

# **Installation**

Follow these steps to install the Inkscape Metaball Extension:

### 1. Download the Extension Files
You'll need the extension files. If you downloaded a `.zip` or `.tar.gz` archive, extract its contents to a temporary folder. You should find files like `metaball.py` and `metaball.inx` (and potentially others).

### 2. Locate Your Inkscape Extensions Folder
The location of your Inkscape extensions folder varies depending on your operating system:
 
- Windows:

   Typically **`C:\Program Files\Inkscape\share\inkscape\extensions\`**

   Alternatively, for user-specific extensions:**` %APPDATA%\Inkscape\extensions\`** (you can  type **` %APPDATA% `** directly into the Windows Explorer address bar).

- macOS:

   ` /Applications/Inkscape.app/Contents/Resources/share/inkscape/extensions/`
   
   Alternatively, for user-specific extensions: `~/.config/inkscape/extensions/` or `~/Library/Application Support/org.inkscape.Inkscape/config/inkscape/extensions/` (depending on your Inkscape version and installation method).

- Linux:

  `/usr/share/inkscape/extensions/` (system-wide)

  `~/.config/inkscape/extensions/` (user-specific)

 Tip: You can often find the path to your user extensions folder directly within Inkscape. Go to `Edit > Preferences > System` and look for `"User extensions".`

### 3. Copy the Extension Files
Copy the **`metaball.py`** and **`metaball.inx`** files (and any other accompanying files from the extension) into the Inkscape extensions folder you located in the previous step.

### 4. Restart Inkscape
After copying the files, you must restart **`Inkscape`** for the new extension to be recognized. Close all open Inkscape windows and then launch it again.

### 5. Verify Installation
To check if the installation was successful:

a). Open **`Inkscape`**.

b). Go to **`Extensions`** in the main menu.

c). Look for a new entry related to **`Metaball`** (e.g., **`Render > Metaballs`**).

## Find Extension:- ` Extension > Render > Metaballs`

If you see the new entry, the installation was successful!

# Usage

To use the Metaball extension:

-  Create multiple overlapping shapes (e.g., circles, ellipses).

- Select all the shapes and Group , you want to include in the metaball effect. 

- Go to **`Extensions` > `Render` > `Metaballs`**.

- Adjust the settings (**`Radius` , `Alpha Threshold`**) in the dialog box that appears and click "**`Apply`**".
