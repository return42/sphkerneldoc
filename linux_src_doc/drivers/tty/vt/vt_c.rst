.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/vt/vt.c

.. _`vc_do_resize`:

vc_do_resize
============

.. c:function:: int vc_do_resize(struct tty_struct *tty, struct vc_data *vc, unsigned int cols, unsigned int lines)

    resizing method for the tty

    :param struct tty_struct \*tty:
        tty being resized

    :param struct vc_data \*vc:
        virtual console private data

    :param unsigned int cols:
        columns

    :param unsigned int lines:
        lines

.. _`vc_do_resize.description`:

Description
-----------

Resize a virtual console, clipping according to the actual constraints.
If the caller passes a tty structure then update the termios winsize
information and perform any necessary signal handling.

Caller must hold the console semaphore. Takes the termios rwsem and
ctrl_lock of the tty IFF a tty is passed.

.. _`vc_resize`:

vc_resize
=========

.. c:function:: int vc_resize(struct vc_data *vc, unsigned int cols, unsigned int rows)

    resize a VT

    :param struct vc_data \*vc:
        virtual console

    :param unsigned int cols:
        columns

    :param unsigned int rows:
        rows

.. _`vc_resize.description`:

Description
-----------

Resize a virtual console as seen from the console end of things. We
use the common vc_do_resize methods to update the structures. The
caller must hold the console sem to protect console internals and
vc->port.tty

.. _`vt_resize`:

vt_resize
=========

.. c:function:: int vt_resize(struct tty_struct *tty, struct winsize *ws)

    resize a VT

    :param struct tty_struct \*tty:
        tty to resize

    :param struct winsize \*ws:
        winsize attributes

.. _`vt_resize.description`:

Description
-----------

Resize a virtual terminal. This is called by the tty layer as we
register our own handler for resizing. The mutual helper does all
the actual work.

Takes the console sem and the called methods then take the tty
termios_rwsem and the tty ctrl_lock in that order.

.. _`vt_kmsg_redirect`:

vt_kmsg_redirect
================

.. c:function:: int vt_kmsg_redirect(int new)

    Sets/gets the kernel message console

    :param int new:
        The new virtual terminal number or -1 if the console should stay
        unchanged

.. _`vt_kmsg_redirect.description`:

Description
-----------

By default, the kernel messages are always printed on the current virtual
console. However, the user may modify that default with the
TIOCL_SETKMSGREDIRECT ioctl call.

This function sets the kernel message console to be \ ``new``\ . It returns the old
virtual console number. The virtual terminal number 0 (both as parameter and
return value) means no redirection (i.e. always printed on the currently
active console).

The parameter -1 means that only the current console is returned, but the
value is not modified. You may use the macro \ :c:func:`vt_get_kmsg_redirect`\  in that
case to make the code more understandable.

When the kernel is compiled without CONFIG_VT_CONSOLE, this function ignores
the parameter and always returns 0.

.. _`con_is_bound`:

con_is_bound
============

.. c:function:: int con_is_bound(const struct consw *csw)

    checks if driver is bound to the console

    :param const struct consw \*csw:
        console driver

.. _`con_is_bound.return`:

Return
------

zero if unbound, nonzero if bound

Drivers can call this and if zero, they should release
all resources allocated on \ :c:func:`con_startup`\ 

.. _`con_debug_enter`:

con_debug_enter
===============

.. c:function:: int con_debug_enter(struct vc_data *vc)

    prepare the console for the kernel debugger

    :param struct vc_data \*vc:
        *undescribed*

.. _`con_debug_enter.description`:

Description
-----------

Called when the console is taken over by the kernel debugger, this
function needs to save the current console state, then put the console
into a state suitable for the kernel debugger.

.. _`con_debug_enter.return`:

Return
------

Zero on success, nonzero if a failure occurred when trying to prepare
the console for the debugger.

.. _`con_debug_leave`:

con_debug_leave
===============

.. c:function:: int con_debug_leave( void)

    restore console state

    :param  void:
        no arguments

.. _`con_debug_leave.description`:

Description
-----------

Restore the console state to what it was before the kernel debugger
was invoked.

.. _`con_debug_leave.return`:

Return
------

Zero on success, nonzero if a failure occurred when trying to restore
the console.

.. _`do_unregister_con_driver`:

do_unregister_con_driver
========================

.. c:function:: int do_unregister_con_driver(const struct consw *csw)

    unregister console driver from console layer

    :param const struct consw \*csw:
        console driver

.. _`do_unregister_con_driver.description`:

Description
-----------

All drivers that registers to the console layer must
call this function upon exit, or if the console driver is in a state
where it won't be able to handle console services, such as the
framebuffer console without loaded framebuffer drivers.

The driver must unbind first prior to unregistration.

.. This file was automatic generated / don't edit.

