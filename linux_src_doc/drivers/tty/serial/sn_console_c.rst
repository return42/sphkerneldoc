.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/serial/sn_console.c

.. _`snt_poll_getc`:

snt_poll_getc
=============

.. c:function:: int snt_poll_getc( void)

    Get a character from the console in polling mode

    :param  void:
        no arguments

.. _`snt_poll_input_pending`:

snt_poll_input_pending
======================

.. c:function:: int snt_poll_input_pending( void)

    Check if any input is waiting - polling mode.

    :param  void:
        no arguments

.. _`snt_intr_getc`:

snt_intr_getc
=============

.. c:function:: int snt_intr_getc( void)

    Get a character from the console, interrupt mode

    :param  void:
        no arguments

.. _`snt_intr_input_pending`:

snt_intr_input_pending
======================

.. c:function:: int snt_intr_input_pending( void)

    Check if input is pending, interrupt mode

    :param  void:
        no arguments

.. _`snt_hw_puts_raw`:

snt_hw_puts_raw
===============

.. c:function:: int snt_hw_puts_raw(const char *s, int len)

    Send raw string to the console, polled or interrupt mode

    :param const char \*s:
        String

    :param int len:
        Length

.. _`snt_hw_puts_buffered`:

snt_hw_puts_buffered
====================

.. c:function:: int snt_hw_puts_buffered(const char *s, int len)

    Send string to console, polled or interrupt mode

    :param const char \*s:
        String

    :param int len:
        Length

.. _`snp_type`:

snp_type
========

.. c:function:: const char *snp_type(struct uart_port *port)

    What type of console are we?

    :param struct uart_port \*port:
        Port to operate with (we ignore since we only have one port)

.. _`snp_tx_empty`:

snp_tx_empty
============

.. c:function:: unsigned int snp_tx_empty(struct uart_port *port)

    Is the transmitter empty?  We pretend we're always empty

    :param struct uart_port \*port:
        Port to operate on (we ignore since we only have one port)

.. _`snp_stop_tx`:

snp_stop_tx
===========

.. c:function:: void snp_stop_tx(struct uart_port *port)

    stop the transmitter - no-op for us

    :param struct uart_port \*port:
        Port to operat eon - we ignore - no-op function

.. _`snp_release_port`:

snp_release_port
================

.. c:function:: void snp_release_port(struct uart_port *port)

    Free i/o and resources for port - no-op for us

    :param struct uart_port \*port:
        Port to operate on - we ignore - no-op function

.. _`snp_shutdown`:

snp_shutdown
============

.. c:function:: void snp_shutdown(struct uart_port *port)

    shut down the port - free irq and disable - no-op for us

    :param struct uart_port \*port:
        Port to shut down - we ignore

.. _`snp_set_mctrl`:

snp_set_mctrl
=============

.. c:function:: void snp_set_mctrl(struct uart_port *port, unsigned int mctrl)

    set control lines (dtr, rts, etc) - no-op for our console

    :param struct uart_port \*port:
        Port to operate on - we ignore

    :param unsigned int mctrl:
        Lines to set/unset - we ignore

.. _`snp_get_mctrl`:

snp_get_mctrl
=============

.. c:function:: unsigned int snp_get_mctrl(struct uart_port *port)

    get contorl line info, we just return a static value

    :param struct uart_port \*port:
        port to operate on - we only have one port so we ignore this

.. _`snp_stop_rx`:

snp_stop_rx
===========

.. c:function:: void snp_stop_rx(struct uart_port *port)

    Stop the receiver - we ignor ethis

    :param struct uart_port \*port:
        Port to operate on - we ignore

.. _`snp_start_tx`:

snp_start_tx
============

.. c:function:: void snp_start_tx(struct uart_port *port)

    Start transmitter

    :param struct uart_port \*port:
        Port to operate on

.. _`snp_break_ctl`:

snp_break_ctl
=============

.. c:function:: void snp_break_ctl(struct uart_port *port, int break_state)

    handle breaks - ignored by us

    :param struct uart_port \*port:
        Port to operate on

    :param int break_state:
        Break state

.. _`snp_startup`:

snp_startup
===========

.. c:function:: int snp_startup(struct uart_port *port)

    Start up the serial port - always return 0 (We're always on)

    :param struct uart_port \*port:
        Port to operate on

.. _`snp_set_termios`:

snp_set_termios
===============

.. c:function:: void snp_set_termios(struct uart_port *port, struct ktermios *termios, struct ktermios *old)

    set termios stuff - we ignore these

    :param struct uart_port \*port:
        port to operate on

    :param struct ktermios \*termios:
        Old

    :param struct ktermios \*old:
        *undescribed*

.. _`snp_request_port`:

snp_request_port
================

.. c:function:: int snp_request_port(struct uart_port *port)

    allocate resources for port - ignored by us

    :param struct uart_port \*port:
        port to operate on

.. _`snp_config_port`:

snp_config_port
===============

.. c:function:: void snp_config_port(struct uart_port *port, int flags)

    allocate resources, set up - we ignore,  we're always on

    :param struct uart_port \*port:
        Port to operate on

    :param int flags:
        flags used for port setup

.. _`sn_debug_printf`:

sn_debug_printf
===============

.. c:function:: int sn_debug_printf(const char *fmt,  ...)

    close to hardware debugging printf

    :param const char \*fmt:
        printf format

    :param ellipsis ellipsis:
        variable arguments

.. _`sn_debug_printf.description`:

Description
-----------

This is as "close to the metal" as we can get, used when the driver
itself may be broken.

.. _`sn_receive_chars`:

sn_receive_chars
================

.. c:function:: void sn_receive_chars(struct sn_cons_port *port, unsigned long flags)

    Grab characters, pass them to tty layer

    :param struct sn_cons_port \*port:
        Port to operate on

    :param unsigned long flags:
        irq flags

.. _`sn_receive_chars.note`:

Note
----

If we're not registered with the serial core infrastructure yet,
we don't try to send characters to it...

.. _`sn_transmit_chars`:

sn_transmit_chars
=================

.. c:function:: void sn_transmit_chars(struct sn_cons_port *port, int raw)

    grab characters from serial core, send off

    :param struct sn_cons_port \*port:
        Port to operate on

    :param int raw:
        Transmit raw or buffered

.. _`sn_transmit_chars.note`:

Note
----

If we're early, before we're registered with serial core, the
writes are going through sn_sal_console_write because that's how
register_console has been set up.  We currently could have asynch
polls calling this function due to sn_sal_switch_to_asynch but we can
ignore them until we register with the serial core stuffs.

.. _`sn_sal_interrupt`:

sn_sal_interrupt
================

.. c:function:: irqreturn_t sn_sal_interrupt(int irq, void *dev_id)

    Handle console interrupts

    :param int irq:
        irq #, useful for debug statements

    :param void \*dev_id:
        our pointer to our port (sn_cons_port which contains the uart port)

.. _`sn_sal_timer_poll`:

sn_sal_timer_poll
=================

.. c:function:: void sn_sal_timer_poll(unsigned long data)

    this function handles polled console mode

    :param unsigned long data:
        A pointer to our sn_cons_port (which contains the uart port)

.. _`sn_sal_timer_poll.description`:

Description
-----------

data is the pointer that init_timer will store for us.  This function is
associated with init_timer to see if there is any console traffic.
Obviously not used in interrupt mode

.. _`sn_sal_switch_to_asynch`:

sn_sal_switch_to_asynch
=======================

.. c:function:: void sn_sal_switch_to_asynch(struct sn_cons_port *port)

    Switch to async mode (as opposed to synch)

    :param struct sn_cons_port \*port:
        Our sn_cons_port (which contains the uart port)

.. _`sn_sal_switch_to_asynch.description`:

Description
-----------

So this is used by sn_sal_serial_console_init (early on, before we're
registered with serial core).  It's also used by sn_sal_init
right after we've registered with serial core.  The later only happens
if we didn't already come through here via sn_sal_serial_console_init.

.. _`sn_sal_switch_to_interrupts`:

sn_sal_switch_to_interrupts
===========================

.. c:function:: void sn_sal_switch_to_interrupts(struct sn_cons_port *port)

    Switch to interrupt driven mode

    :param struct sn_cons_port \*port:
        Our sn_cons_port (which contains the uart port)

.. _`sn_sal_switch_to_interrupts.description`:

Description
-----------

In sn_sal_init, after we're registered with serial core and
the port is added, this function is called to switch us to interrupt
mode.  We were previously in asynch/polling mode (using init_timer).

We attempt to switch to interrupt mode here by calling
request_irq.  If that works out, we enable receive interrupts.

.. _`sn_sal_init`:

sn_sal_init
===========

.. c:function:: int sn_sal_init( void)

    When the kernel loads us, get us rolling w/ serial core

    :param  void:
        no arguments

.. _`sn_sal_init.description`:

Description
-----------

Before this is called, we've been printing kernel messages in a special
early mode not making use of the serial core infrastructure.  When our
driver is loaded for real, we register the driver and port with serial
core and try to enable interrupt driven mode.

.. _`puts_raw_fixed`:

puts_raw_fixed
==============

.. c:function:: void puts_raw_fixed(int (*puts_raw)(const char *s, int len), const char *s, int count)

    sn_sal_console_write helper for adding \r's as required

    :param int (\*puts_raw)(const char \*s, int len):
        puts function to do the writing

    :param const char \*s:
        input string

    :param int count:
        length

.. _`puts_raw_fixed.description`:

Description
-----------

We need a \r ahead of every \n for direct writes through
ia64_sn_console_putb (what sal_puts_raw below actually does).

.. _`sn_sal_console_write`:

sn_sal_console_write
====================

.. c:function:: void sn_sal_console_write(struct console *co, const char *s, unsigned count)

    Print statements before serial core available

    :param struct console \*co:
        *undescribed*

    :param const char \*s:
        String to send

    :param unsigned count:
        length

.. _`sn_sal_console_write.description`:

Description
-----------

This is referenced in the console struct.  It is used for early
console printing before we register with serial core and for things
such as kdb.  The console_lock must be held when we get here.

This function has some code for trying to print output even if the lock
is held.  We try to cover the case where a lock holder could have died.
We don't use this special case code if we're not registered with serial
core yet.  After we're registered with serial core, the only time this
function would be used is for high level kernel output like magic sys req,
kdb, and printk's.

.. _`sn_sal_console_setup`:

sn_sal_console_setup
====================

.. c:function:: int sn_sal_console_setup(struct console *co, char *options)

    Set up console for early printing

    :param struct console \*co:
        Console to work with

    :param char \*options:
        Options to set

.. _`sn_sal_console_setup.description`:

Description
-----------

Altix console doesn't do anything with baud rates, etc, anyway.

This isn't required since not providing the setup function in the
console struct is ok.  However, other patches like KDB plop something
here so providing it is easier.

.. _`sn_sal_console_write_early`:

sn_sal_console_write_early
==========================

.. c:function:: void sn_sal_console_write_early(struct console *co, const char *s, unsigned count)

    simple early output routine \ ``co``\  - console struct \ ``s``\  - string to print \ ``count``\  - count

    :param struct console \*co:
        *undescribed*

    :param const char \*s:
        *undescribed*

    :param unsigned count:
        *undescribed*

.. _`sn_sal_console_write_early.description`:

Description
-----------

Simple function to provide early output, before even
sn_sal_serial_console_init is called.  Referenced in the
console struct registerd in sn_serial_console_early_setup.

.. _`sn_serial_console_early_setup`:

sn_serial_console_early_setup
=============================

.. c:function:: int sn_serial_console_early_setup( void)

    Sets up early console output support

    :param  void:
        no arguments

.. _`sn_serial_console_early_setup.description`:

Description
-----------

Register a console early on...  This is for output before even
sn_sal_serial_cosnole_init is called.  This function is called from
setup.c.  This allows us to do really early polled writes. When
sn_sal_serial_console_init is called, this console is unregistered
and a new one registered.

.. _`sn_sal_serial_console_init`:

sn_sal_serial_console_init
==========================

.. c:function:: int sn_sal_serial_console_init( void)

    Early console output - set up for register

    :param  void:
        no arguments

.. _`sn_sal_serial_console_init.description`:

Description
-----------

This function is called when regular console init happens.  Because we
support even earlier console output with sn_serial_console_early_setup
(called from setup.c directly), this function unregisters the really
early console.

.. _`sn_sal_serial_console_init.note`:

Note
----

Even if setup.c doesn't register sal_console_early, unregistering
it here doesn't hurt anything.

.. This file was automatic generated / don't edit.

