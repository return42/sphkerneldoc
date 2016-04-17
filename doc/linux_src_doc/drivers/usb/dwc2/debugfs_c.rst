.. -*- coding: utf-8; mode: rst -*-

=========
debugfs.c
=========


.. _`testmode_write`:

testmode_write
==============

.. c:function:: ssize_t testmode_write (struct file *file, const char __user *ubuf, size_t count, loff_t *ppos)

    Designware USB2 DRD controller debugfs

    :param struct file \*file:

        *undescribed*

    :param const char __user \*ubuf:

        *undescribed*

    :param size_t count:

        *undescribed*

    :param loff_t \*ppos:

        *undescribed*



.. _`testmode_write.description`:

Description
-----------


Copyright (C) 2015 Intel Corporation
Mian Yousaf Kaukab <yousaf.kaukab\ ``intel``\ .com>



.. _`testmode_write.this-program-is-free-software`:

This program is free software
-----------------------------

you can redistribute it and/or modify
it under the terms of the GNU General Public License version 2  of
the License as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.



.. _`testmode_show`:

testmode_show
=============

.. c:function:: int testmode_show (struct seq_file *s, void *unused)

    debugfs: show usb test mode state

    :param struct seq_file \*s:

        *undescribed*

    :param void \*unused:

        *undescribed*



.. _`testmode_show.description`:

Description
-----------

This debugfs entry shows which usb test mode is currently enabled.



.. _`state_show`:

state_show
==========

.. c:function:: int state_show (struct seq_file *seq, void *v)

    debugfs: show overall driver and device state.

    :param struct seq_file \*seq:
        The seq file to write to.

    :param void \*v:
        Unused parameter.



.. _`state_show.description`:

Description
-----------

This debugfs entry shows the overall state of the hardware and
some general information about each of the endpoints available
to the system.



.. _`fifo_show`:

fifo_show
=========

.. c:function:: int fifo_show (struct seq_file *seq, void *v)

    debugfs: show the fifo information

    :param struct seq_file \*seq:
        The seq_file to write data to.

    :param void \*v:
        Unused parameter.



.. _`fifo_show.description`:

Description
-----------

Show the FIFO information for the overall fifo and all the
periodic transmission FIFOs.



.. _`ep_show`:

ep_show
=======

.. c:function:: int ep_show (struct seq_file *seq, void *v)

    debugfs: show the state of an endpoint.

    :param struct seq_file \*seq:
        The seq_file to write data to.

    :param void \*v:
        Unused parameter.



.. _`ep_show.description`:

Description
-----------

This debugfs entry shows the state of the given endpoint (one is
registered for each available).



.. _`dwc2_hsotg_create_debug`:

dwc2_hsotg_create_debug
=======================

.. c:function:: void dwc2_hsotg_create_debug (struct dwc2_hsotg *hsotg)

    create debugfs directory and files

    :param struct dwc2_hsotg \*hsotg:
        The driver state



.. _`dwc2_hsotg_create_debug.description`:

Description
-----------

Create the debugfs files to allow the user to get information
about the state of the system. The directory name is created
with the same name as the device itself, in case we end up
with multiple blocks in future systems.

