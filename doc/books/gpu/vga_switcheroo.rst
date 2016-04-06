
.. _vga_switcheroo:

++++++++++++++
vga_switcheroo
++++++++++++++
vga_switcheroo is the Linux subsystem for laptop hybrid graphics. These come in two flavors:

⋆ muxed: Dual GPUs with a multiplexer chip to switch outputs between GPUs. ⋆ muxless: Dual GPUs but only one of them is connected to outputs. The other one is merely used to
offload rendering, its results are copied over PCIe into the framebuffer. On Linux this is supported with DRI PRIME.

Hybrid graphics started to appear in the late Naughties and were initially all muxed. Newer laptops moved to a muxless architecture for cost reasons. A notable exception is the
MacBook Pro which continues to use a mux. Muxes come with varying capabilities: Some switch only the panel, others can also switch external displays. Some switch all display pins
at once while others can switch just the DDC lines. (To allow EDID probing for the inactive GPU.) Also, muxes are often used to cut power to the discrete GPU while it is not used.

DRM drivers register GPUs with vga_switcheroo, these are henceforth called clients. The mux is called the handler. Muxless machines also register a handler to control the power
state of the discrete GPU, its ->switchto callback is a no-op for obvious reasons. The discrete GPU is often equipped with an HDA controller for the HDMI/DP audio signal, this will
also register as a client so that vga_switcheroo can take care of the correct suspend/resume order when changing the discrete GPU's power state. In total there can thus be up to
three clients: Two vga clients (GPUs) and one audio client (on the discrete GPU). The code is mostly prepared to support machines with more than two GPUs should they become
available.

The GPU to which the outputs are currently switched is called the active client in vga_switcheroo parlance. The GPU not in use is the inactive client. When the inactive client's
DRM driver is loaded, it will be unable to probe the panel's EDID and hence depends on VBIOS to provide its display modes. If the VBIOS modes are bogus or if there is no VBIOS at
all (which is common on the MacBook Pro), a client may alternatively request that the DDC lines are temporarily switched to it, provided that the handler supports this. Switching
only the DDC lines and not the entire output avoids unnecessary flickering.


.. toctree::
    :maxdepth: 1

    modes_of_use
    api
    handlers
