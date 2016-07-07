.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/pti.c

.. _`pti_write_to_aperture`:

pti_write_to_aperture
=====================

.. c:function:: void pti_write_to_aperture(struct pti_masterchannel *mc, u8 *buf, int len)

    The private write function to PTI HW.

    :param struct pti_masterchannel \*mc:
        The 'aperture'. It's part of a write address that holds
        a master and channel ID.

    :param u8 \*buf:
        Data being written to the HW that will ultimately be seen
        in a debugging tool (Fido, Lauterbach).

    :param int len:
        Size of buffer.

.. _`pti_write_to_aperture.description`:

Description
-----------

Since each aperture is specified by a unique
master/channel ID, no two processes will be writing
to the same aperture at the same time so no lock is required. The
PTI-Output agent will send these out in the order that they arrived, and
thus, it will intermix these messages. The debug tool can then later
regroup the appropriate message segments together reconstituting each
message.

.. _`pti_control_frame_built_and_sent`:

pti_control_frame_built_and_sent
================================

.. c:function:: void pti_control_frame_built_and_sent(struct pti_masterchannel *mc, const char *thread_name)

    control frame build and send function.

    :param struct pti_masterchannel \*mc:
        The master / channel structure on which the function
        built a control frame.

    :param const char \*thread_name:
        The thread name associated with the master / channel or
        'NULL' if using the 'current' global variable.

.. _`pti_control_frame_built_and_sent.description`:

Description
-----------

To be able to post process the PTI contents on host side, a control frame
is added before sending any PTI content. So the host side knows on
each PTI frame the name of the thread using a dedicated master / channel.
The thread name is retrieved from 'current' global variable if 'thread_name'
is 'NULL', else it is retrieved from 'thread_name' parameter.
This function builds this frame and sends it to a master ID CONTROL_ID.
The overhead is only 32 bytes since the driver only writes to HW
in 32 byte chunks.

.. _`pti_write_full_frame_to_aperture`:

pti_write_full_frame_to_aperture
================================

.. c:function:: void pti_write_full_frame_to_aperture(struct pti_masterchannel *mc, const unsigned char *buf, int len)

    high level function to write to PTI.

    :param struct pti_masterchannel \*mc:
        The 'aperture'. It's part of a write address that holds
        a master and channel ID.

    :param const unsigned char \*buf:
        Data being written to the HW that will ultimately be seen
        in a debugging tool (Fido, Lauterbach).

    :param int len:
        Size of buffer.

.. _`pti_write_full_frame_to_aperture.description`:

Description
-----------

All threads sending data (either console, user space application, ...)
are calling the high level function to write to PTI meaning that it is
possible to add a control frame before sending the content.

.. _`get_id`:

get_id
======

.. c:function:: struct pti_masterchannel *get_id(u8 *id_array, int max_ids, int base_id, const char *thread_name)

    Allocate a master and channel ID.

    :param u8 \*id_array:
        an array of bits representing what channel
        id's are allocated for writing.

    :param int max_ids:
        The max amount of available write IDs to use.

    :param int base_id:
        The starting SW channel ID, based on the Intel
        PTI arch.

    :param const char \*thread_name:
        The thread name associated with the master / channel or
        'NULL' if using the 'current' global variable.

.. _`get_id.return`:

Return
------

pti_masterchannel struct with master, channel ID address
0 for error

Each bit in the arrays ia_app and ia_os correspond to a master and
channel id. The bit is one if the id is taken and 0 if free. For
every master there are 128 channel id's.

.. _`pti_request_masterchannel`:

pti_request_masterchannel
=========================

.. c:function:: struct pti_masterchannel *pti_request_masterchannel(u8 type, const char *thread_name)

    Kernel API function used to allocate a master, channel ID address to write to PTI HW.

    :param u8 type:
        0- request Application  master, channel aperture ID
        write address.
        1- request OS master, channel aperture ID write
        address.
        2- request Modem master, channel aperture ID
        write address.
        Other values, error.

    :param const char \*thread_name:
        The thread name associated with the master / channel or
        'NULL' if using the 'current' global variable.

.. _`pti_request_masterchannel.return`:

Return
------

pti_masterchannel struct
0 for error

.. _`pti_release_masterchannel`:

pti_release_masterchannel
=========================

.. c:function:: void pti_release_masterchannel(struct pti_masterchannel *mc)

    Kernel API function used to release a master, channel ID address used to write to PTI HW.

    :param struct pti_masterchannel \*mc:
        master, channel apeture ID address to be released.  This
        will de-allocate the structure via \ :c:func:`kfree`\ .

.. _`pti_writedata`:

pti_writedata
=============

.. c:function:: void pti_writedata(struct pti_masterchannel *mc, u8 *buf, int count)

    Kernel API function used to write trace debugging data to PTI HW.

    :param struct pti_masterchannel \*mc:
        Master, channel aperture ID address to write to.
        Null value will return with no write occurring.

    :param u8 \*buf:
        Trace debuging data to write to the PTI HW.
        Null value will return with no write occurring.

    :param int count:
        Size of buf. Value of 0 or a negative number will
        return with no write occuring.

.. _`pti_tty_driver_open`:

pti_tty_driver_open
===================

.. c:function:: int pti_tty_driver_open(struct tty_struct *tty, struct file *filp)

    Open an Application master, channel aperture ID to the PTI device via tty device.

    :param struct tty_struct \*tty:
        tty interface.

    :param struct file \*filp:
        filp interface pased to \ :c:func:`tty_port_open`\  call.

.. _`pti_tty_driver_open.return`:

Return
------

int, 0 for success
otherwise, fail value

The main purpose of using the tty device interface is for
each tty port to have a unique PTI write aperture.  In an
example use case, ttyPTI0 gets syslogd and an APP aperture
ID and ttyPTI1 is where the n_tracesink ldisc hooks to route
modem messages into PTI.  Modem trace data does not have to
go to ttyPTI1, but ttyPTI0 and ttyPTI1 do need to be distinct
master IDs.  These messages go through the PTI HW and out of
the handheld platform and to the Fido/Lauterbach device.

.. _`pti_tty_driver_close`:

pti_tty_driver_close
====================

.. c:function:: void pti_tty_driver_close(struct tty_struct *tty, struct file *filp)

    close tty device and release Application master, channel aperture ID to the PTI device via tty device.

    :param struct tty_struct \*tty:
        tty interface.

    :param struct file \*filp:
        filp interface pased to \ :c:func:`tty_port_close`\  call.

.. _`pti_tty_driver_close.description`:

Description
-----------

The main purpose of using the tty device interface is to route
syslog daemon messages to the PTI HW and out of the handheld platform
and to the Fido/Lauterbach device.

.. _`pti_tty_install`:

pti_tty_install
===============

.. c:function:: int pti_tty_install(struct tty_driver *driver, struct tty_struct *tty)

    Used to set up specific master-channels to tty ports for organizational purposes when tracing viewed from debuging tools.

    :param struct tty_driver \*driver:
        tty driver information.

    :param struct tty_struct \*tty:
        tty struct containing pti information.

.. _`pti_tty_install.return`:

Return
------

0 for success
otherwise, error

.. _`pti_tty_cleanup`:

pti_tty_cleanup
===============

.. c:function:: void pti_tty_cleanup(struct tty_struct *tty)

    Used to de-allocate master-channel resources tied to tty's of this driver.

    :param struct tty_struct \*tty:
        tty struct containing pti information.

.. _`pti_tty_driver_write`:

pti_tty_driver_write
====================

.. c:function:: int pti_tty_driver_write(struct tty_struct *tty, const unsigned char *buf, int len)

    Write trace debugging data through the char interface to the PTI HW.  Part of the misc device implementation.

    :param struct tty_struct \*tty:
        *undescribed*

    :param const unsigned char \*buf:
        *undescribed*

    :param int len:
        # of byte to write.

.. _`pti_tty_driver_write.return`:

Return
------

int, # of bytes written
otherwise, error

.. _`pti_tty_write_room`:

pti_tty_write_room
==================

.. c:function:: int pti_tty_write_room(struct tty_struct *tty)

    Always returns 2048.

    :param struct tty_struct \*tty:
        contains tty info of the pti driver.

.. _`pti_char_open`:

pti_char_open
=============

.. c:function:: int pti_char_open(struct inode *inode, struct file *filp)

    Open an Application master, channel aperture ID to the PTI device. Part of the misc device implementation.

    :param struct inode \*inode:
        not used.

    :param struct file \*filp:
        Output- will have a masterchannel struct set containing
        the allocated application PTI aperture write address.

.. _`pti_char_open.return`:

Return
------

int, 0 for success
otherwise, a fail value

.. _`pti_char_release`:

pti_char_release
================

.. c:function:: int pti_char_release(struct inode *inode, struct file *filp)

    Close a char channel to the PTI device. Part of the misc device implementation.

    :param struct inode \*inode:
        Not used in this implementaiton.

    :param struct file \*filp:
        Contains private_data that contains the master, channel
        ID to be released by the PTI device.

.. _`pti_char_release.return`:

Return
------

always 0

.. _`pti_char_write`:

pti_char_write
==============

.. c:function:: ssize_t pti_char_write(struct file *filp, const char __user *data, size_t len, loff_t *ppose)

    Write trace debugging data through the char interface to the PTI HW.  Part of the misc device implementation.

    :param struct file \*filp:
        Contains private data which is used to obtain
        master, channel write ID.

    :param const char __user \*data:
        trace data to be written.

    :param size_t len:
        # of byte to write.

    :param loff_t \*ppose:
        Not used in this function implementation.

.. _`pti_char_write.return`:

Return
------

int, # of bytes written
otherwise, error value

.. _`pti_char_write.notes`:

Notes
-----

From side discussions with Alan Cox and experimenting
with PTI debug HW like Nokia's Fido box and Lauterbach
devices, 8192 byte write buffer used by USER_COPY_SIZE was
deemed an appropriate size for this type of usage with
debugging HW.

.. _`pti_console_write`:

pti_console_write
=================

.. c:function:: void pti_console_write(struct console *c, const char *buf, unsigned len)

    Write to the console that has been acquired.

    :param struct console \*c:
        Not used in this implementaiton.

    :param const char \*buf:
        Data to be written.

    :param unsigned len:
        Length of buf.

.. _`pti_console_device`:

pti_console_device
==================

.. c:function:: struct tty_driver *pti_console_device(struct console *c, int *index)

    Return the driver tty structure and set the associated index implementation.

    :param struct console \*c:
        Console device of the driver.

    :param int \*index:
        index associated with c.

.. _`pti_console_device.return`:

Return
------

always value of pti_tty_driver structure when this function
is called.

.. _`pti_console_setup`:

pti_console_setup
=================

.. c:function:: int pti_console_setup(struct console *c, char *opts)

    Initialize console variables used by the driver.

    :param struct console \*c:
        Not used.

    :param char \*opts:
        Not used.

.. _`pti_console_setup.return`:

Return
------

always 0.

.. _`pti_port_activate`:

pti_port_activate
=================

.. c:function:: int pti_port_activate(struct tty_port *port, struct tty_struct *tty)

    Used to start/initialize any items upon first opening of \ :c:func:`tty_port`\ .

    :param struct tty_port \*port:
        *undescribed*

    :param struct tty_struct \*tty:
        *undescribed*

.. _`pti_port_activate.description`:

Description
-----------

\ ``port``\ - The tty port number of the PTI device.
\ ``tty``\ -  The tty struct associated with this device.

.. _`pti_port_activate.return`:

Return
------

always returns 0

.. _`pti_port_activate.notes`:

Notes
-----

The primary purpose of the PTI tty port 0 is to hook
the syslog daemon to it; thus this port will be open for a
very long time.

.. _`pti_port_shutdown`:

pti_port_shutdown
=================

.. c:function:: void pti_port_shutdown(struct tty_port *port)

    Used to stop/shutdown any items upon the last tty port close.

    :param struct tty_port \*port:
        *undescribed*

.. _`pti_port_shutdown.description`:

Description
-----------

\ ``port``\ - The tty port number of the PTI device.

.. _`pti_port_shutdown.notes`:

Notes
-----

The primary purpose of the PTI tty port 0 is to hook
the syslog daemon to it; thus this port will be open for a
very long time.

.. _`pti_pci_probe`:

pti_pci_probe
=============

.. c:function:: int pti_pci_probe(struct pci_dev *pdev, const struct pci_device_id *ent)

    Used to detect pti on the pci bus and set things up in the driver.

    :param struct pci_dev \*pdev:
        *undescribed*

    :param const struct pci_device_id \*ent:
        *undescribed*

.. _`pti_pci_probe.description`:

Description
-----------

\ ``pdev``\ - pci_dev struct values for pti.
\ ``ent``\ -  pci_device_id struct for pti driver.

.. _`pti_pci_probe.return`:

Return
------

0 for success
otherwise, error

.. _`pti_pci_remove`:

pti_pci_remove
==============

.. c:function:: void pti_pci_remove(struct pci_dev *pdev)

    Driver exit method to remove PTI from PCI bus.

    :param struct pci_dev \*pdev:
        variable containing pci info of PTI.

.. _`pti_exit`:

pti_exit
========

.. c:function:: void __exit pti_exit( void)

    Unregisters this module as a tty and pci driver.

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

