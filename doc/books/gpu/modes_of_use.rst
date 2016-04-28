.. -*- coding: utf-8; mode: rst -*-

.. _modes_of_use:

============
Modes of Use
============


Manual switching and manual power control
=========================================

In this mode of use, the file /sys/kernel/debug/vgaswitcheroo/switch can
be read to retrieve the current vga_switcheroo state and commands can
be written to it to change the state. The file appears as soon as two
GPU drivers and one handler have registered with vga_switcheroo. The
following commands are understood:

* OFF: Power off the device not in use. * ON: Power on the device not in
use. * IGD: Switch to the integrated graphics device. Power on the
integrated GPU if necessary, power off the discrete GPU. Prerequisite is
that no user space processes (e.g. Xorg, alsactl) have opened device
files of the GPUs or the audio client. If the switch fails, the user may
invoke lsof(8) or fuser(1) on /dev/dri/ and /dev/snd/controlC1 to
identify processes blocking the switch. * DIS: Switch to the discrete
graphics device. * DIGD: Delayed switch to the integrated graphics
device. This will perform the switch once the last user space process
has closed the device files of the GPUs and the audio client. * DDIS:
Delayed switch to the discrete graphics device. * MIGD: Mux-only switch
to the integrated graphics device. Does not remap console or change the
power state of either gpu. If the integrated GPU is currently off, the
screen will turn black. If it is on, the screen will show whatever
happens to be in VRAM. Either way, the user has to blindly enter the
command to switch back. * MDIS: Mux-only switch to the discrete graphics
device.

For GPUs whose power state is controlled by the driver's runtime pm, the
ON and OFF commands are a no-op (see next section).

For muxless machines, the IGD/DIS, DIGD/DDIS and MIGD/MDIS commands
should not be used.


Driver power control
====================

In this mode of use, the discrete GPU automatically powers up and down
at the discretion of the driver's runtime pm. On muxed machines, the
user may still influence the muxer state by way of the debugfs
interface, however the ON and OFF commands become a no-op for the
discrete GPU.

This mode is the default on Nvidia HybridPower/Optimus and ATI
PowerXpress. Specifying nouveau.runpm=0, radeon.runpm=0 or
amdgpu.runpm=0 on the kernel command line disables it.

When the driver decides to power up or down, it notifies vga_switcheroo
thereof so that it can (a) power the audio device on the GPU up or down,
and (b) update its internal power state representation for the device.
This is achieved by ``vga_switcheroo_set_dynamic_switch``.

After the GPU has been suspended, the handler needs to be called to cut
power to the GPU. Likewise it needs to reinstate power before the GPU
can resume. This is achieved by ``vga_switcheroo_init_domain_pm_ops``,
which augments the GPU's suspend/resume functions by the requisite calls
to the handler.

When the audio device resumes, the GPU needs to be woken. This is
achieved by ``vga_switcheroo_init_domain_pm_optimus_hdmi_audio``, which
augments the audio device's resume function.

On muxed machines, if the mux is initially switched to the discrete GPU,
the user ends up with a black screen when the GPU powers down after
boot. As a workaround, the mux is forced to the integrated GPU on
runtime suspend, cf. https://bugs.freedesktop.org/show_bug.cgi?id=75917


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
