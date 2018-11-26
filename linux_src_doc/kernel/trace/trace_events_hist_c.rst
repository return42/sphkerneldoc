.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/trace/trace_events_hist.c

.. _`create_field_var_hist`:

create_field_var_hist
=====================

.. c:function:: struct hist_field *create_field_var_hist(struct hist_trigger_data *target_hist_data, char *subsys_name, char *event_name, char *field_name)

    Automatically create a histogram and var for a field

    :param target_hist_data:
        The target hist trigger
    :type target_hist_data: struct hist_trigger_data \*

    :param subsys_name:
        Optional subsystem name
    :type subsys_name: char \*

    :param event_name:
        Optional event name
    :type event_name: char \*

    :param field_name:
        The name of the field (and the resulting variable)
    :type field_name: char \*

.. _`create_field_var_hist.description`:

Description
-----------

Hist trigger actions fetch data from variables, not directly from
events.  However, for convenience, users are allowed to directly
specify an event field in an action, which will be automatically
converted into a variable on their behalf.
If a user specifies a field on an event that isn't the event the
histogram currently being defined (the target event histogram), the
only way that can be accomplished is if a new hist trigger is
created and the field variable defined on that.

This function creates a new histogram compatible with the target
event (meaning a histogram with the same key as the target
histogram), and creates a variable for the specified field, but
with 'synthetic_' prepended to the variable name in order to avoid
collision with normal field variables.

.. _`create_field_var_hist.return`:

Return
------

The variable created for the field.

.. _`create_target_field_var`:

create_target_field_var
=======================

.. c:function:: struct field_var *create_target_field_var(struct hist_trigger_data *target_hist_data, char *subsys_name, char *event_name, char *var_name)

    Automatically create a variable for a field

    :param target_hist_data:
        The target hist trigger
    :type target_hist_data: struct hist_trigger_data \*

    :param subsys_name:
        Optional subsystem name
    :type subsys_name: char \*

    :param event_name:
        Optional event name
    :type event_name: char \*

    :param var_name:
        The name of the field (and the resulting variable)
    :type var_name: char \*

.. _`create_target_field_var.description`:

Description
-----------

Hist trigger actions fetch data from variables, not directly from
events.  However, for convenience, users are allowed to directly
specify an event field in an action, which will be automatically
converted into a variable on their behalf.
This function creates a field variable with the name var_name on
the hist trigger currently being defined on the target event.  If
subsys_name and event_name are specified, this function simply
verifies that they do in fact match the target event subsystem and
event name.

.. _`create_target_field_var.return`:

Return
------

The variable created for the field.

.. This file was automatic generated / don't edit.

