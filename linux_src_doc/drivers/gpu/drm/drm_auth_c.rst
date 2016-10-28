.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_auth.c

.. _`drm_getmagic`:

drm_getmagic
============

.. c:function:: int drm_getmagic(struct drm_device *dev, void *data, struct drm_file *file_priv)

    Get unique magic of a client

    :param struct drm_device \*dev:
        DRM device to operate on

    :param void \*data:
        ioctl data containing the drm_auth object

    :param struct drm_file \*file_priv:
        DRM file that performs the operation

.. _`drm_getmagic.description`:

Description
-----------

This looks up the unique magic of the passed client and returns it. If the
client did not have a magic assigned, yet, a new one is registered. The magic
is stored in the passed drm_auth object.

.. _`drm_getmagic.return`:

Return
------

0 on success, negative error code on failure.

.. _`drm_authmagic`:

drm_authmagic
=============

.. c:function:: int drm_authmagic(struct drm_device *dev, void *data, struct drm_file *file_priv)

    Authenticate client with a magic

    :param struct drm_device \*dev:
        DRM device to operate on

    :param void \*data:
        ioctl data containing the drm_auth object

    :param struct drm_file \*file_priv:
        DRM file that performs the operation

.. _`drm_authmagic.description`:

Description
-----------

This looks up a DRM client by the passed magic and authenticates it.

.. _`drm_authmagic.return`:

Return
------

0 on success, negative error code on failure.

.. This file was automatic generated / don't edit.

