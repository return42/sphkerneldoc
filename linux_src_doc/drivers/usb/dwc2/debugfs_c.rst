.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/dwc2/debugfs.c

.. _`testmode_write`:

testmode_write
==============

.. c:function:: ssize_t testmode_write(struct file *file, const char __user *ubuf, size_t count, loff_t *ppos)

    change usb test mode state.

    :param struct file \*file:
        The  file to write to.

    :param const char __user \*ubuf:
        The buffer where user wrote.

    :param size_t count:
        The ubuf size.

    :param loff_t \*ppos:
        Unused parameter.

.. _`testmode_show`:

testmode_show
=============

.. c:function:: int testmode_show(struct seq_file *s, void *unused)

    debugfs: show usb test mode state

    :param struct seq_file \*s:
        The seq file to write to.

    :param void \*unused:
        Unused parameter.

.. _`testmode_show.description`:

Description
-----------

This debugfs entry shows which usb test mode is currently enabled.

.. _`state_show`:

state_show
==========

.. c:function:: int state_show(struct seq_file *seq, void *v)

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

.. c:function:: int fifo_show(struct seq_file *seq, void *v)

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

.. c:function:: int ep_show(struct seq_file *seq, void *v)

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

.. c:function:: void dwc2_hsotg_create_debug(struct dwc2_hsotg *hsotg)

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

.. This file was automatic generated / don't edit.

