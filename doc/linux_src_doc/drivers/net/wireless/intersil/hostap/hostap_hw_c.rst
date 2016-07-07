.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intersil/hostap/hostap_hw.c

.. _`__hostap_cmd_queue_free`:

__hostap_cmd_queue_free
=======================

.. c:function:: void __hostap_cmd_queue_free(local_info_t *local, struct hostap_cmd_queue *entry, int del_req)

    Free Prism2 command queue entry (private)

    :param local_info_t \*local:
        pointer to private Host AP driver data

    :param struct hostap_cmd_queue \*entry:
        Prism2 command queue entry to be freed

    :param int del_req:
        request the entry to be removed

.. _`__hostap_cmd_queue_free.description`:

Description
-----------

Internal helper function for freeing Prism2 command queue entries.
Caller must have acquired local->cmdlock before calling this function.

.. _`hostap_cmd_queue_free`:

hostap_cmd_queue_free
=====================

.. c:function:: void hostap_cmd_queue_free(local_info_t *local, struct hostap_cmd_queue *entry, int del_req)

    Free Prism2 command queue entry

    :param local_info_t \*local:
        pointer to private Host AP driver data

    :param struct hostap_cmd_queue \*entry:
        Prism2 command queue entry to be freed

    :param int del_req:
        request the entry to be removed

.. _`hostap_cmd_queue_free.description`:

Description
-----------

Free a Prism2 command queue entry.

.. _`prism2_clear_cmd_queue`:

prism2_clear_cmd_queue
======================

.. c:function:: void prism2_clear_cmd_queue(local_info_t *local)

    Free all pending Prism2 command queue entries

    :param local_info_t \*local:
        pointer to private Host AP driver data

.. _`hfa384x_cmd_issue`:

hfa384x_cmd_issue
=================

.. c:function:: int hfa384x_cmd_issue(struct net_device *dev, struct hostap_cmd_queue *entry)

    Issue a Prism2 command to the hardware

    :param struct net_device \*dev:
        pointer to net_device

    :param struct hostap_cmd_queue \*entry:
        Prism2 command queue entry to be issued

.. _`hfa384x_cmd`:

hfa384x_cmd
===========

.. c:function:: int hfa384x_cmd(struct net_device *dev, u16 cmd, u16 param0, u16 *param1, u16 *resp0)

    Issue a Prism2 command and wait (sleep) for completion

    :param struct net_device \*dev:
        pointer to net_device

    :param u16 cmd:
        Prism2 command code (HFA384X_CMD_CODE\_\*)

    :param u16 param0:
        value for Param0 register

    :param u16 \*param1:
        value for Param1 register (pointer; \ ``NULL``\  if not used)

    :param u16 \*resp0:
        pointer for Resp0 data or \ ``NULL``\  if Resp0 is not needed

.. _`hfa384x_cmd.description`:

Description
-----------

Issue given command (possibly after waiting in command queue) and sleep
until the command is completed (or timed out or interrupted). This can be
called only from user process context.

.. _`hfa384x_cmd_callback`:

hfa384x_cmd_callback
====================

.. c:function:: int hfa384x_cmd_callback(struct net_device *dev, u16 cmd, u16 param0, void (*) callback (struct net_device *dev, long context, u16 resp0, u16 status, long context)

    Issue a Prism2 command; callback when completed

    :param struct net_device \*dev:
        pointer to net_device

    :param u16 cmd:
        Prism2 command code (HFA384X_CMD_CODE\_\*)

    :param u16 param0:
        value for Param0 register

    :param (void (\*) callback (struct net_device \*dev, long context, u16 resp0, u16 status):
        command completion callback function (\ ``NULL``\  = no callback)

    :param long context:
        context data to be given to the callback function

.. _`hfa384x_cmd_callback.description`:

Description
-----------

Issue given command (possibly after waiting in command queue) and use
callback function to indicate command completion. This can be called both
from user and interrupt context. The callback function will be called in
hardware IRQ context. It can be \ ``NULL``\ , when no function is called when
command is completed.

.. _`__hfa384x_cmd_no_wait`:

__hfa384x_cmd_no_wait
=====================

.. c:function:: int __hfa384x_cmd_no_wait(struct net_device *dev, u16 cmd, u16 param0, int io_debug_num)

    Issue a Prism2 command (private)

    :param struct net_device \*dev:
        pointer to net_device

    :param u16 cmd:
        Prism2 command code (HFA384X_CMD_CODE\_\*)

    :param u16 param0:
        value for Param0 register

    :param int io_debug_num:
        I/O debug error number

.. _`__hfa384x_cmd_no_wait.description`:

Description
-----------

Shared helper function for \ :c:func:`hfa384x_cmd_wait`\  and \ :c:func:`hfa384x_cmd_no_wait`\ .

.. _`hfa384x_cmd_wait`:

hfa384x_cmd_wait
================

.. c:function:: int hfa384x_cmd_wait(struct net_device *dev, u16 cmd, u16 param0)

    Issue a Prism2 command and busy wait for completion

    :param struct net_device \*dev:
        pointer to net_device

    :param u16 cmd:
        Prism2 command code (HFA384X_CMD_CODE\_\*)

    :param u16 param0:
        value for Param0 register

.. _`hfa384x_cmd_no_wait`:

hfa384x_cmd_no_wait
===================

.. c:function:: int hfa384x_cmd_no_wait(struct net_device *dev, u16 cmd, u16 param0)

    Issue a Prism2 command; do not wait for completion

    :param struct net_device \*dev:
        pointer to net_device

    :param u16 cmd:
        Prism2 command code (HFA384X_CMD_CODE\_\*)

    :param u16 param0:
        value for Param0 register

.. _`prism2_cmd_ev`:

prism2_cmd_ev
=============

.. c:function:: void prism2_cmd_ev(struct net_device *dev)

    Prism2 command completion event handler

    :param struct net_device \*dev:
        pointer to net_device

.. _`prism2_cmd_ev.description`:

Description
-----------

Interrupt handler for command completion events. Called by the main
interrupt handler in hardware IRQ context. Read Resp0 and status registers
from the hardware and ACK the event. Depending on the issued command type
either wake up the sleeping process that is waiting for command completion
or call the callback function. Issue the next command, if one is pending.

.. This file was automatic generated / don't edit.

