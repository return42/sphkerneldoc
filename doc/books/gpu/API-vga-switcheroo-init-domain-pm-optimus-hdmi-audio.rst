
.. _API-vga-switcheroo-init-domain-pm-optimus-hdmi-audio:

================================================
vga_switcheroo_init_domain_pm_optimus_hdmi_audio
================================================

*man vga_switcheroo_init_domain_pm_optimus_hdmi_audio(9)*

*4.6.0-rc1*

helper for driver power control


Synopsis
========

.. c:function:: int vga_switcheroo_init_domain_pm_optimus_hdmi_audio( struct device * dev, struct dev_pm_domain * domain )

Arguments
=========

``dev``
    audio client device

``domain``
    power domain


Description
===========

Helper for GPUs whose power state is controlled by the driver's runtime pm. When the audio device resumes, the GPU needs to be woken. This helper augments the audio device's resume
function to do that.


Return
======

0 on success, -EINVAL if no power management operations are defined for this device.
