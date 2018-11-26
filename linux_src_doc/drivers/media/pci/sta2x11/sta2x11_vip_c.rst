.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/pci/sta2x11/sta2x11_vip.c

.. _`sta2x11_vip`:

struct sta2x11_vip
==================

.. c:type:: struct sta2x11_vip

    All internal data for one instance of device

.. _`sta2x11_vip.definition`:

Definition
----------

.. code-block:: c

    struct sta2x11_vip {
        struct v4l2_device v4l2_dev;
        struct video_device video_dev;
        struct pci_dev *pdev;
        struct i2c_adapter *adapter;
        unsigned int register_save_area[IRQ_COUNT + SAVE_COUNT + AUX_COUNT];
        struct v4l2_subdev *decoder;
        struct v4l2_ctrl_handler ctrl_hdl;
        struct v4l2_pix_format format;
        v4l2_std_id std;
        unsigned int input;
        int disabled;
        spinlock_t slock;
        struct vb2_queue vb_vidq;
        struct list_head buffer_list;
        unsigned int sequence;
        struct vip_buffer *active;
        spinlock_t lock;
        struct mutex v4l_lock;
        int tcount, bcount;
        int overflow;
        void __iomem *iomem;
        struct vip_config *config;
    }

.. _`sta2x11_vip.members`:

Members
-------

v4l2_dev
    device registered in v4l layer

video_dev
    properties of our device

pdev
    PCI device

adapter
    contains I2C adapter information

register_save_area
    All relevant register are saved here during suspend

decoder
    contains information about video DAC

ctrl_hdl
    handler for control framework

format
    pixel format, fixed UYVY

std
    video standard (e.g. PAL/NTSC)

input
    input line for video signal ( 0 or 1 )

disabled
    Device is in power down state

slock
    for excluse acces of registers

vb_vidq
    queue maintained by videobuf2 layer

buffer_list
    list of buffer in use

sequence
    sequence number of acquired buffer

active
    current active buffer

lock
    used in videobuf2 callback

v4l_lock
    serialize its video4linux ioctls

tcount
    Number of top frames

bcount
    Number of bottom frames

overflow
    Number of FIFO overflows

iomem
    hardware base address

config
    I2C and gpio config from platform

.. _`sta2x11_vip.description`:

Description
-----------

All non-local data is accessed via this structure.

.. _`vidioc_querycap`:

vidioc_querycap
===============

.. c:function:: int vidioc_querycap(struct file *file, void *priv, struct v4l2_capability *cap)

    return capabilities of device

    :param file:
        descriptor of device
    :type file: struct file \*

    :param priv:
        unused
    :type priv: void \*

    :param cap:
        contains return values
    :type cap: struct v4l2_capability \*

.. _`vidioc_querycap.description`:

Description
-----------

the capabilities of the device are returned

.. _`vidioc_querycap.return-value`:

return value
------------

0, no error.

.. _`vidioc_s_std`:

vidioc_s_std
============

.. c:function:: int vidioc_s_std(struct file *file, void *priv, v4l2_std_id std)

    set video standard

    :param file:
        descriptor of device
    :type file: struct file \*

    :param priv:
        unused
    :type priv: void \*

    :param std:
        contains standard to be set
    :type std: v4l2_std_id

.. _`vidioc_s_std.description`:

Description
-----------

the video standard is set

.. _`vidioc_s_std.return-value`:

return value
------------

0, no error.

-EIO, no input signal detected

other, returned from video DAC.

.. _`vidioc_g_std`:

vidioc_g_std
============

.. c:function:: int vidioc_g_std(struct file *file, void *priv, v4l2_std_id *std)

    get video standard

    :param file:
        descriptor of device
    :type file: struct file \*

    :param priv:
        unused
    :type priv: void \*

    :param std:
        contains return values
    :type std: v4l2_std_id \*

.. _`vidioc_g_std.description`:

Description
-----------

the current video standard is returned

.. _`vidioc_g_std.return-value`:

return value
------------

0, no error.

.. _`vidioc_querystd`:

vidioc_querystd
===============

.. c:function:: int vidioc_querystd(struct file *file, void *priv, v4l2_std_id *std)

    get possible video standards

    :param file:
        descriptor of device
    :type file: struct file \*

    :param priv:
        unused
    :type priv: void \*

    :param std:
        contains return values
    :type std: v4l2_std_id \*

.. _`vidioc_querystd.description`:

Description
-----------

all possible video standards are returned

.. _`vidioc_querystd.return-value`:

return value
------------

delivered by video DAC routine.

.. _`vidioc_s_input`:

vidioc_s_input
==============

.. c:function:: int vidioc_s_input(struct file *file, void *priv, unsigned int i)

    set input line

    :param file:
        descriptor of device
    :type file: struct file \*

    :param priv:
        unused
    :type priv: void \*

    :param i:
        new input line number
    :type i: unsigned int

.. _`vidioc_s_input.description`:

Description
-----------

the current active input line is set

.. _`vidioc_s_input.return-value`:

return value
------------

0, no error.

-EINVAL, line number out of range

.. _`vidioc_g_input`:

vidioc_g_input
==============

.. c:function:: int vidioc_g_input(struct file *file, void *priv, unsigned int *i)

    return input line

    :param file:
        descriptor of device
    :type file: struct file \*

    :param priv:
        unused
    :type priv: void \*

    :param i:
        returned input line number
    :type i: unsigned int \*

.. _`vidioc_g_input.description`:

Description
-----------

the current active input line is returned

.. _`vidioc_g_input.return-value`:

return value
------------

always 0.

.. _`vidioc_enum_fmt_vid_cap`:

vidioc_enum_fmt_vid_cap
=======================

.. c:function:: int vidioc_enum_fmt_vid_cap(struct file *file, void *priv, struct v4l2_fmtdesc *f)

    return video capture format

    :param file:
        descriptor of device
    :type file: struct file \*

    :param priv:
        unused
    :type priv: void \*

    :param f:
        returned format information
    :type f: struct v4l2_fmtdesc \*

.. _`vidioc_enum_fmt_vid_cap.description`:

Description
-----------

returns name and format of video capture
Only UYVY is supported by hardware.

.. _`vidioc_enum_fmt_vid_cap.return-value`:

return value
------------

always 0.

.. _`vidioc_try_fmt_vid_cap`:

vidioc_try_fmt_vid_cap
======================

.. c:function:: int vidioc_try_fmt_vid_cap(struct file *file, void *priv, struct v4l2_format *f)

    set video capture format

    :param file:
        descriptor of device
    :type file: struct file \*

    :param priv:
        unused
    :type priv: void \*

    :param f:
        new format
    :type f: struct v4l2_format \*

.. _`vidioc_try_fmt_vid_cap.description`:

Description
-----------

new video format is set which includes width and
field type. width is fixed to 720, no scaling.
Only UYVY is supported by this hardware.
the minimum height is 200, the maximum is 576 (PAL)

.. _`vidioc_try_fmt_vid_cap.return-value`:

return value
------------

0, no error

-EINVAL, pixel or field format not supported

.. _`vidioc_s_fmt_vid_cap`:

vidioc_s_fmt_vid_cap
====================

.. c:function:: int vidioc_s_fmt_vid_cap(struct file *file, void *priv, struct v4l2_format *f)

    set current video format parameters

    :param file:
        descriptor of device
    :type file: struct file \*

    :param priv:
        unused
    :type priv: void \*

    :param f:
        returned format information
    :type f: struct v4l2_format \*

.. _`vidioc_s_fmt_vid_cap.description`:

Description
-----------

set new capture format

.. _`vidioc_s_fmt_vid_cap.return-value`:

return value
------------

0, no error

other, delivered by video DAC routine.

.. _`vidioc_g_fmt_vid_cap`:

vidioc_g_fmt_vid_cap
====================

.. c:function:: int vidioc_g_fmt_vid_cap(struct file *file, void *priv, struct v4l2_format *f)

    get current video format parameters

    :param file:
        descriptor of device
    :type file: struct file \*

    :param priv:
        unused
    :type priv: void \*

    :param f:
        contains format information
    :type f: struct v4l2_format \*

.. _`vidioc_g_fmt_vid_cap.description`:

Description
-----------

returns current video format parameters

.. _`vidioc_g_fmt_vid_cap.return-value`:

return value
------------

0, always successful

.. _`vip_irq`:

vip_irq
=======

.. c:function:: irqreturn_t vip_irq(int irq, struct sta2x11_vip *vip)

    interrupt routine

    :param irq:
        Number of interrupt ( not used, correct number is assumed )
    :type irq: int

    :param vip:
        local data structure containing all information
    :type vip: struct sta2x11_vip \*

.. _`vip_irq.description`:

Description
-----------

check for both frame interrupts set ( top and bottom ).
check FIFO overflow, but limit number of log messages after open.
signal a complete buffer if done

.. _`vip_irq.return-value`:

return value
------------

IRQ_NONE, interrupt was not generated by VIP

IRQ_HANDLED, interrupt done.

.. _`vip_gpio_reserve`:

vip_gpio_reserve
================

.. c:function:: int vip_gpio_reserve(struct device *dev, int pin, int dir, const char *name)

    reserve gpio pin

    :param dev:
        device
    :type dev: struct device \*

    :param pin:
        GPIO pin number
    :type pin: int

    :param dir:
        direction, input or output
    :type dir: int

    :param name:
        GPIO pin name
    :type name: const char \*

.. _`vip_gpio_release`:

vip_gpio_release
================

.. c:function:: void vip_gpio_release(struct device *dev, int pin, const char *name)

    release gpio pin

    :param dev:
        device
    :type dev: struct device \*

    :param pin:
        GPIO pin number
    :type pin: int

    :param name:
        GPIO pin name
    :type name: const char \*

.. _`sta2x11_vip_init_one`:

sta2x11_vip_init_one
====================

.. c:function:: int sta2x11_vip_init_one(struct pci_dev *pdev, const struct pci_device_id *ent)

    init one instance of video device

    :param pdev:
        PCI device
    :type pdev: struct pci_dev \*

    :param ent:
        (not used)
    :type ent: const struct pci_device_id \*

.. _`sta2x11_vip_init_one.description`:

Description
-----------

allocate reset pins for DAC.
Reset video DAC, this is done via reset line.
allocate memory for managing device
request interrupt
map IO region
register device
find and initialize video DAC

.. _`sta2x11_vip_init_one.return-value`:

return value
------------

0, no error

-ENOMEM, no memory

-ENODEV, device could not be detected or registered

.. _`sta2x11_vip_remove_one`:

sta2x11_vip_remove_one
======================

.. c:function:: void sta2x11_vip_remove_one(struct pci_dev *pdev)

    release device

    :param pdev:
        PCI device
    :type pdev: struct pci_dev \*

.. _`sta2x11_vip_remove_one.description`:

Description
-----------

Undo everything done in .._init_one

unregister video device
free interrupt
unmap ioadresses
free memory
free GPIO pins

.. _`sta2x11_vip_suspend`:

sta2x11_vip_suspend
===================

.. c:function:: int sta2x11_vip_suspend(struct pci_dev *pdev, pm_message_t state)

    set device into power save mode

    :param pdev:
        PCI device
    :type pdev: struct pci_dev \*

    :param state:
        new state of device
    :type state: pm_message_t

.. _`sta2x11_vip_suspend.description`:

Description
-----------

all relevant registers are saved and an attempt to set a new state is made.

.. _`sta2x11_vip_suspend.return-value`:

return value
------------

0 always indicate success,
even if device could not be disabled. (workaround for hardware problem)

.. _`sta2x11_vip_resume`:

sta2x11_vip_resume
==================

.. c:function:: int sta2x11_vip_resume(struct pci_dev *pdev)

    resume device operation

    :param pdev:
        PCI device
    :type pdev: struct pci_dev \*

.. _`sta2x11_vip_resume.description`:

Description
-----------

re-enable device, set PCI state to powered and restore registers.
resume normal device operation afterwards.

.. _`sta2x11_vip_resume.return-value`:

return value
------------

0, no error.

other, could not set device to power on state.

.. This file was automatic generated / don't edit.

