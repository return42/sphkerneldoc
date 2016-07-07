.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/9p/v9fs.c

.. _`v9fs_parse_options`:

v9fs_parse_options
==================

.. c:function:: int v9fs_parse_options(struct v9fs_session_info *v9ses, char *opts)

    parse mount options into session structure

    :param struct v9fs_session_info \*v9ses:
        existing v9fs session information

    :param char \*opts:
        *undescribed*

.. _`v9fs_parse_options.description`:

Description
-----------

Return 0 upon success, -ERRNO upon failure.

.. _`v9fs_session_init`:

v9fs_session_init
=================

.. c:function:: struct p9_fid *v9fs_session_init(struct v9fs_session_info *v9ses, const char *dev_name, char *data)

    initialize session

    :param struct v9fs_session_info \*v9ses:
        session information structure

    :param const char \*dev_name:
        device being mounted

    :param char \*data:
        options

.. _`v9fs_session_close`:

v9fs_session_close
==================

.. c:function:: void v9fs_session_close(struct v9fs_session_info *v9ses)

    shutdown a session

    :param struct v9fs_session_info \*v9ses:
        session information structure

.. _`v9fs_session_cancel`:

v9fs_session_cancel
===================

.. c:function:: void v9fs_session_cancel(struct v9fs_session_info *v9ses)

    terminate a session

    :param struct v9fs_session_info \*v9ses:
        session to terminate

.. _`v9fs_session_cancel.description`:

Description
-----------

mark transport as disconnected and cancel all pending requests.

.. _`v9fs_session_begin_cancel`:

v9fs_session_begin_cancel
=========================

.. c:function:: void v9fs_session_begin_cancel(struct v9fs_session_info *v9ses)

    Begin terminate of a session

    :param struct v9fs_session_info \*v9ses:
        session to terminate

.. _`v9fs_session_begin_cancel.description`:

Description
-----------

After this call we don't allow any request other than clunk.

.. _`caches_show`:

caches_show
===========

.. c:function:: ssize_t caches_show(struct kobject *kobj, struct kobj_attribute *attr, char *buf)

    list caches associated with a session

    :param struct kobject \*kobj:
        *undescribed*

    :param struct kobj_attribute \*attr:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`caches_show.description`:

Description
-----------

Returns the size of buffer written.

.. _`v9fs_sysfs_init`:

v9fs_sysfs_init
===============

.. c:function:: int v9fs_sysfs_init( void)

    Initialize the v9fs sysfs interface

    :param  void:
        no arguments

.. _`v9fs_sysfs_cleanup`:

v9fs_sysfs_cleanup
==================

.. c:function:: void v9fs_sysfs_cleanup( void)

    Unregister the v9fs sysfs interface

    :param  void:
        no arguments

.. _`v9fs_init_inode_cache`:

v9fs_init_inode_cache
=====================

.. c:function:: int v9fs_init_inode_cache( void)

    initialize a cache for 9P Returns 0 on success.

    :param  void:
        no arguments

.. _`v9fs_destroy_inode_cache`:

v9fs_destroy_inode_cache
========================

.. c:function:: void v9fs_destroy_inode_cache( void)

    destroy the cache of 9P inode

    :param  void:
        no arguments

.. _`init_v9fs`:

init_v9fs
=========

.. c:function:: int init_v9fs( void)

    Initialize module

    :param  void:
        no arguments

.. _`exit_v9fs`:

exit_v9fs
=========

.. c:function:: void __exit exit_v9fs( void)

    shutdown module

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

