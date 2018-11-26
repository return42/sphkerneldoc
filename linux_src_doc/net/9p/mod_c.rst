.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/9p/mod.c

.. _`v9fs_register_trans`:

v9fs_register_trans
===================

.. c:function:: void v9fs_register_trans(struct p9_trans_module *m)

    register a new transport with 9p

    :param m:
        structure describing the transport module and entry points
    :type m: struct p9_trans_module \*

.. _`v9fs_unregister_trans`:

v9fs_unregister_trans
=====================

.. c:function:: void v9fs_unregister_trans(struct p9_trans_module *m)

    unregister a 9p transport

    :param m:
        the transport to remove
    :type m: struct p9_trans_module \*

.. _`v9fs_get_trans_by_name`:

v9fs_get_trans_by_name
======================

.. c:function:: struct p9_trans_module *v9fs_get_trans_by_name(char *s)

    get transport with the matching name

    :param s:
        string identifying transport
    :type s: char \*

.. _`v9fs_get_default_trans`:

v9fs_get_default_trans
======================

.. c:function:: struct p9_trans_module *v9fs_get_default_trans( void)

    get the default transport

    :param void:
        no arguments
    :type void: 

.. _`v9fs_put_trans`:

v9fs_put_trans
==============

.. c:function:: void v9fs_put_trans(struct p9_trans_module *m)

    put trans

    :param m:
        transport to put
    :type m: struct p9_trans_module \*

.. _`init_p9`:

init_p9
=======

.. c:function:: int init_p9( void)

    Initialize module

    :param void:
        no arguments
    :type void: 

.. _`exit_p9`:

exit_p9
=======

.. c:function:: void __exit exit_p9( void)

    shutdown module

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

