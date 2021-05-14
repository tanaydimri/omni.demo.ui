**[NOT OFFICIAL FROM NVIDIA]**

This is a demo extension with UI to understand how Omniverse Extension are structured.

To run this demo extension, put this in one of your Omniverse extension search paths. I prefere to put it under: "..\Documents\Kit\shared\exts" Then search for "demo" in your extensions tab, in any of the Omniverse applications.

**Some important points to notice:**
- The core functionality of the extension lives in demo/core. Here an init file in responsible for "collecting" all the core modules to be important by other modules.
- Likewise, the UI related code lives under demo/ui
- All the classes inheriting from "omni.ext.IExt" will be instantiated at the time when an extension is enabled and will automatically call the on_startup method. Besides, it will also call on_shutdown on extension disable.
- Be sure to read about Omni UI styling. There is a great documentation in your Omni Kit app, under Omni::UI Doc.

---
Hope this helps you with building your own extensions :)
- Stay Safe!!
