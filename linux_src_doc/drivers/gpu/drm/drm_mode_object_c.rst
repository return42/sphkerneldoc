.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_mode_object.c

.. _`drm_mode_object_get`:

drm_mode_object_get
===================

.. c:function:: int drm_mode_object_get(struct drm_device *dev, struct drm_mode_object *obj, uint32_t obj_type)

    allocate a new modeset identifier

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_mode_object \*obj:
        object pointer, used to generate unique ID

    :param uint32_t obj_type:
        object type

.. _`drm_mode_object_get.description`:

Description
-----------

Create a unique identifier based on \ ``ptr``\  in \ ``dev``\ 's identifier space.  Used
for tracking modes, CRTCs and connectors. Note that despite the _get postfix
modeset identifiers are _not_ reference counted. Hence don't use this for
reference counted modeset objects like framebuffers.

.. _`drm_mode_object_get.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_mode_object_unregister`:

drm_mode_object_unregister
==========================

.. c:function:: void drm_mode_object_unregister(struct drm_device *dev, struct drm_mode_object *object)

    free a modeset identifer

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_mode_object \*object:
        object to free

.. _`drm_mode_object_unregister.description`:

Description
-----------

Free \ ``id``\  from \ ``dev``\ 's unique identifier pool.
This function can be called multiple times, and guards against
multiple removals.
These modeset identifiers are _not_ reference counted. Hence don't use this
for reference counted modeset objects like framebuffers.

.. _`drm_mode_object_find`:

drm_mode_object_find
====================

.. c:function:: struct drm_mode_object *drm_mode_object_find(struct drm_device *dev, uint32_t id, uint32_t type)

    look up a drm object with static lifetime

    :param struct drm_device \*dev:
        drm device

    :param uint32_t id:
        id of the mode object

    :param uint32_t type:
        type of the mode object

.. _`drm_mode_object_find.description`:

Description
-----------

This function is used to look up a modeset object. It will acquire a
reference for reference counted objects. This reference must be dropped again
by callind \ :c:func:`drm_mode_object_unreference`\ .

.. _`drm_mode_object_unreference`:

drm_mode_object_unreference
===========================

.. c:function:: void drm_mode_object_unreference(struct drm_mode_object *obj)

    decr the object refcnt

    :param struct drm_mode_object \*obj:
        mode_object

.. _`drm_mode_object_unreference.description`:

Description
-----------

This function decrements the object's refcount if it is a refcounted modeset
object. It is a no-op on any other object. This is used to drop references
acquired with \ :c:func:`drm_mode_object_reference`\ .

.. _`drm_mode_object_reference`:

drm_mode_object_reference
=========================

.. c:function:: void drm_mode_object_reference(struct drm_mode_object *obj)

    incr the object refcnt

    :param struct drm_mode_object \*obj:
        mode_object

.. _`drm_mode_object_reference.description`:

Description
-----------

This function increments the object's refcount if it is a refcounted modeset
object. It is a no-op on any other object. References should be dropped again
by calling \ :c:func:`drm_mode_object_unreference`\ .

.. _`drm_object_attach_property`:

drm_object_attach_property
==========================

.. c:function:: void drm_object_attach_property(struct drm_mode_object *obj, struct drm_property *property, uint64_t init_val)

    attach a property to a modeset object

    :param struct drm_mode_object \*obj:
        drm modeset object

    :param struct drm_property \*property:
        property to attach

    :param uint64_t init_val:
        initial value of the property

.. _`drm_object_attach_property.description`:

Description
-----------

This attaches the given property to the modeset object with the given initial
value. Currently this function cannot fail since the properties are stored in
a statically sized array.

.. _`drm_object_property_set_value`:

drm_object_property_set_value
=============================

.. c:function:: int drm_object_property_set_value(struct drm_mode_object *obj, struct drm_property *property, uint64_t val)

    set the value of a property

    :param struct drm_mode_object \*obj:
        drm mode object to set property value for

    :param struct drm_property \*property:
        property to set

    :param uint64_t val:
        value the property should be set to

.. _`drm_object_property_set_value.description`:

Description
-----------

This function sets a given property on a given object. This function only
changes the software state of the property, it does not call into the
driver's ->set_property callback.

Note that atomic drivers should not have any need to call this, the core will
ensure consistency of values reported back to userspace through the
appropriate ->atomic_get_property callback. Only legacy drivers should call
this function to update the tracked value (after clamping and other
restrictions have been applied).

.. _`drm_object_property_set_value.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_object_property_get_value`:

drm_object_property_get_value
=============================

.. c:function:: int drm_object_property_get_value(struct drm_mode_object *obj, struct drm_property *property, uint64_t *val)

    retrieve the value of a property

    :param struct drm_mode_object \*obj:
        drm mode object to get property value from

    :param struct drm_property \*property:
        property to retrieve

    :param uint64_t \*val:
        storage for the property value

.. _`drm_object_property_get_value.description`:

Description
-----------

This function retrieves the softare state of the given property for the given
property. Since there is no driver callback to retrieve the current property
value this might be out of sync with the hardware, depending upon the driver
and property.

Atomic drivers should never call this function directly, the core will read
out property values through the various ->atomic_get_property callbacks.

.. _`drm_object_property_get_value.return`:

Return
------

Zero on success, error code on failure.

.. _`drm_mode_obj_get_properties_ioctl`:

drm_mode_obj_get_properties_ioctl
=================================

.. c:function:: int drm_mode_obj_get_properties_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    get the current value of a object's property

    :param struct drm_device \*dev:
        DRM device

    :param void \*data:
        ioctl data

    :param struct drm_file \*file_priv:
        DRM file info

.. _`drm_mode_obj_get_properties_ioctl.description`:

Description
-----------

This function retrieves the current value for an object's property. Compared
to the connector specific ioctl this one is extended to also work on crtc and
plane objects.

Called by the user via ioctl.

.. _`drm_mode_obj_get_properties_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

.. This file was automatic generated / don't edit.
