.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/pti.c

.. _`pti_write_to_aperture`:

pti_write_to_aperture
=====================

.. c:function:: void pti_write_to_aperture(struct pti_masterchannel *mc, u8 *buf, int len)

    The private write function to PTI HW.

    :param mc:
        The 'aperture'. It's part of a write address that holds
        a master and channel ID.
    :type mc: struct pti_masterchannel \*

    :param buf:
        Data being written to the HW that will ultimately be seen
        in a debugging tool (Fido, Lauterbach).
    :type buf: u8 \*

    :param len:
        Size of buffer.
    :type len: int

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

    :param mc:
        The master / channel structure on which the function
        built a control frame.
    :type mc: struct pti_masterchannel \*

    :param thread_name:
        The thread name associated with the master / channel or
        'NULL' if using the 'current' global variable.
    :type thread_name: const char \*

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

    :param mc:
        The 'aperture'. It's part of a write address that holds
        a master and channel ID.
    :type mc: struct pti_masterchannel \*

    :param buf:
        Data being written to the HW that will ultimately be seen
        in a debugging tool (Fido, Lauterbach).
    :type buf: const unsigned char \*

    :param len:
        Size of buffer.
    :type len: int

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

    :param id_array:
        an array of bits representing what channel
        id's are allocated for writing.
    :type id_array: u8 \*

    :param max_ids:
        The max amount of available write IDs to use.
    :type max_ids: int

    :param base_id:
        The starting SW channel ID, based on the Intel
        PTI arch.
    :type base_id: int

    :param thread_name:
        The thread name associated with the master / channel or
        'NULL' if using the 'current' global variable.
    :type thread_name: const char \*

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

    :param type:
        0- request Application  master, channel aperture ID
        write address.
        1- request OS master, channel aperture ID write
        address.
        2- request Modem master, channel aperture ID
        write address.
        Other values, error.
    :type type: u8

    :param thread_name:
        The thread name associated with the master / channel or
        'NULL' if using the 'current' global variable.
    :type thread_name: const char \*

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

    :param mc:
        master, channel apeture ID address to be released.  This
        will de-allocate the structure via \ :c:func:`kfree`\ .
    :type mc: struct pti_masterchannel \*

.. _`pti_writedata`:

pti_writedata
=============

.. c:function:: void pti_writedata(struct pti_masterchannel *mc, u8 *buf, int count)

    Kernel API function used to write trace debugging data to PTI HW.

    :param mc:
        Master, channel aperture ID address to write to.
        Null value will return with no write occurring.
    :type mc: struct pti_masterchannel \*

    :param buf:
        Trace debuging data to write to the PTI HW.
        Null value will return with no write occurring.
    :type buf: u8 \*

    :param count:
        Size of buf. Value of 0 or a negative number will
        return with no write occuring.
    :type count: int

.. _`pti_tty_driver_open`:

pti_tty_driver_open
===================

.. c:function:: int pti_tty_driver_open(struct tty_struct *tty, struct file *filp)

    Open an Application master, channel aperture ID to the PTI device via tty device.

    :param tty:
        tty interface.
    :type tty: struct tty_struct \*

    :param filp:
        filp interface pased to \ :c:func:`tty_port_open`\  call.
    :type filp: struct file \*

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

    :param tty:
        tty interface.
    :type tty: struct tty_struct \*

    :param filp:
        filp interface pased to \ :c:func:`tty_port_close`\  call.
    :type filp: struct file \*

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

    :param driver:
        tty driver information.
    :type driver: struct tty_driver \*

    :param tty:
        tty struct containing pti information.
    :type tty: struct tty_struct \*

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

    :param tty:
        tty struct containing pti information.
    :type tty: struct tty_struct \*

.. _`pti_tty_driver_write`:

pti_tty_driver_write
====================

.. c:function:: int pti_tty_driver_write(struct tty_struct *tty, const unsigned char *buf, int len)

    Write trace debugging data through the char interface to the PTI HW.  Part of the misc device implementation.

    :param tty:
        *undescribed*
    :type tty: struct tty_struct \*

    :param buf:
        *undescribed*
    :type buf: const unsigned char \*

    :param len:
        # of byte to write.
    :type len: int

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

    :param tty:
        contains tty info of the pti driver.
    :type tty: struct tty_struct \*

.. _`pti_char_open`:

pti_char_open
=============

.. c:function:: int pti_char_open(struct inode *inode, struct file *filp)

    Open an Application master, channel aperture ID to the PTI device. Part of the misc device implementation.

    :param inode:
        not used.
    :type inode: struct inode \*

    :param filp:
        Output- will have a masterchannel struct set containing
        the allocated application PTI aperture write address.
    :type filp: struct file \*

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

    :param inode:
        Not used in this implementaiton.
    :type inode: struct inode \*

    :param filp:
        Contains private_data that contains the master, channel
        ID to be released by the PTI device.
    :type filp: struct file \*

.. _`pti_char_release.return`:

Return
------

always 0

.. _`pti_char_write`:

pti_char_write
==============

.. c:function:: ssize_t pti_char_write(struct file *filp, const char __user *data, size_t len, loff_t *ppose)

    Write trace debugging data through the char interface to the PTI HW.  Part of the misc device implementation.

    :param filp:
        Contains private data which is used to obtain
        master, channel write ID.
    :type filp: struct file \*

    :param data:
        trace data to be written.
    :type data: const char __user \*

    :param len:
        # of byte to write.
    :type len: size_t

    :param ppose:
        Not used in this function implementation.
    :type ppose: loff_t \*

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

    :param c:
        Not used in this implementaiton.
    :type c: struct console \*

    :param buf:
        Data to be written.
    :type buf: const char \*

    :param len:
        Length of buf.
    :type len: unsigned

.. _`pti_console_device`:

pti_console_device
==================

.. c:function:: struct tty_driver *pti_console_device(struct console *c, int *index)

    Return the driver tty structure and set the associated index implementation.

    :param c:
        Console device of the driver.
    :type c: struct console \*

    :param index:
        index associated with c.
    :type index: int \*

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

    :param c:
        Not used.
    :type c: struct console \*

    :param opts:
        Not used.
    :type opts: char \*

.. _`pti_console_setup.return`:

Return
------

always 0.

.. _`pti_port_activate`:

pti_port_activate
=================

.. c:function:: int pti_port_activate(struct tty_port *port, struct tty_struct *tty)

    Used to start/initialize any items upon first opening of \ :c:func:`tty_port`\ .

    :param port:
        *undescribed*
    :type port: struct tty_port \*

    :param tty:
        *undescribed*
    :type tty: struct tty_struct \*

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

    :param port:
        *undescribed*
    :type port: struct tty_port \*

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

    :param pdev:
        *undescribed*
    :type pdev: struct pci_dev \*

    :param ent:
        *undescribed*
    :type ent: const struct pci_device_id \*

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

    :param pdev:
        variable containing pci info of PTI.
    :type pdev: struct pci_dev \*

.. _`pti_exit`:

pti_exit
========

.. c:function:: void __exit pti_exit( void)

    Unregisters this module as a tty and pci driver.

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

