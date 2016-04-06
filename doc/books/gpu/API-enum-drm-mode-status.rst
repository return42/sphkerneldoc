
.. _API-enum-drm-mode-status:

====================
enum drm_mode_status
====================

*man enum drm_mode_status(9)*

*4.6.0-rc1*

hardware support status of a mode


Synopsis
========

.. code-block:: c

    enum drm_mode_status {
      MODE_OK,
      MODE_HSYNC,
      MODE_VSYNC,
      MODE_H_ILLEGAL,
      MODE_V_ILLEGAL,
      MODE_BAD_WIDTH,
      MODE_NOMODE,
      MODE_NO_INTERLACE,
      MODE_NO_DBLESCAN,
      MODE_NO_VSCAN,
      MODE_MEM,
      MODE_VIRTUAL_X,
      MODE_VIRTUAL_Y,
      MODE_MEM_VIRT,
      MODE_NOCLOCK,
      MODE_CLOCK_HIGH,
      MODE_CLOCK_LOW,
      MODE_CLOCK_RANGE,
      MODE_BAD_HVALUE,
      MODE_BAD_VVALUE,
      MODE_BAD_VSCAN,
      MODE_HSYNC_NARROW,
      MODE_HSYNC_WIDE,
      MODE_HBLANK_NARROW,
      MODE_HBLANK_WIDE,
      MODE_VSYNC_NARROW,
      MODE_VSYNC_WIDE,
      MODE_VBLANK_NARROW,
      MODE_VBLANK_WIDE,
      MODE_PANEL,
      MODE_INTERLACE_WIDTH,
      MODE_ONE_WIDTH,
      MODE_ONE_HEIGHT,
      MODE_ONE_SIZE,
      MODE_NO_REDUCED,
      MODE_NO_STEREO,
      MODE_STALE,
      MODE_BAD,
      MODE_ERROR
    };


Constants
=========

MODE_OK
    Mode OK

MODE_HSYNC
    hsync out of range

MODE_VSYNC
    vsync out of range

MODE_H_ILLEGAL
    mode has illegal horizontal timings

MODE_V_ILLEGAL
    mode has illegal horizontal timings

MODE_BAD_WIDTH
    requires an unsupported linepitch

MODE_NOMODE
    no mode with a matching name

MODE_NO_INTERLACE
    interlaced mode not supported

MODE_NO_DBLESCAN
    doublescan mode not supported

MODE_NO_VSCAN
    multiscan mode not supported

MODE_MEM
    insufficient video memory

MODE_VIRTUAL_X
    mode width too large for specified virtual size

MODE_VIRTUAL_Y
    mode height too large for specified virtual size

MODE_MEM_VIRT
    insufficient video memory given virtual size

MODE_NOCLOCK
    no fixed clock available

MODE_CLOCK_HIGH
    clock required is too high

MODE_CLOCK_LOW
    clock required is too low

MODE_CLOCK_RANGE
    clock/mode isn't in a ClockRange

MODE_BAD_HVALUE
    horizontal timing was out of range

MODE_BAD_VVALUE
    vertical timing was out of range

MODE_BAD_VSCAN
    VScan value out of range

MODE_HSYNC_NARROW
    horizontal sync too narrow

MODE_HSYNC_WIDE
    horizontal sync too wide

MODE_HBLANK_NARROW
    horizontal blanking too narrow

MODE_HBLANK_WIDE
    horizontal blanking too wide

MODE_VSYNC_NARROW
    vertical sync too narrow

MODE_VSYNC_WIDE
    vertical sync too wide

MODE_VBLANK_NARROW
    vertical blanking too narrow

MODE_VBLANK_WIDE
    vertical blanking too wide

MODE_PANEL
    exceeds panel dimensions

MODE_INTERLACE_WIDTH
    width too large for interlaced mode

MODE_ONE_WIDTH
    only one width is supported

MODE_ONE_HEIGHT
    only one height is supported

MODE_ONE_SIZE
    only one resolution is supported

MODE_NO_REDUCED
    monitor doesn't accept reduced blanking

MODE_NO_STEREO
    stereo modes not supported

MODE_STALE
    mode has become stale

MODE_BAD
    unspecified reason

MODE_ERROR
    error condition


Description
===========

This enum is used to filter out modes not supported by the driver/hardware combination.
