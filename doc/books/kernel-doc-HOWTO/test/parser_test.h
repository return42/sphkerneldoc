/* parse-markup: kernel-doc */

/**
 * struct v4l2_subdev_core_ops - Define core ops callbacks for subdevs
 *
 * @log_status: callback for VIDIOC_LOG_STATUS ioctl handler code.
 *
 * @s_io_pin_config: configure one or more chip I/O pins for chips that
 *      multiplex different internal signal pads out to IO pins.  This function
 *      takes a pointer to an array of 'n' pin configuration entries, one for
 *      each pin being configured.  This function could be called at times
 *      other than just subdevice initialization.
 *
 * @init: initialize the sensor registers to some sort of reasonable default
 *      values. Do not use for new drivers and should be removed in existing
 *      drivers.
 *
 * @load_fw: load firmware.
 *
 * @reset: generic reset command. The argument selects which subsystems to
 *      reset. Passing 0 will always reset the whole chip. Do not use for new
 *      drivers without discussing this first on the linux-media mailinglist.
 *      There should be no reason normally to reset a device.
 *
 * @s_gpio: set GPIO pins. Very simple right now, might need to be extended with
 *      a direction argument if needed.
 *
 * @queryctrl: callback for VIDIOC_QUERYCTL ioctl handler code.
 *
 * @g_ctrl: callback for VIDIOC_G_CTRL ioctl handler code.
 *
 * @s_ctrl: callback for VIDIOC_S_CTRL ioctl handler code.
 *
 * @g_ext_ctrls: callback for VIDIOC_G_EXT_CTRLS ioctl handler code.
 *
 * @s_ext_ctrls: callback for VIDIOC_S_EXT_CTRLS ioctl handler code.
 *
 * @try_ext_ctrls: callback for VIDIOC_TRY_EXT_CTRLS ioctl handler code.
 *
 * @querymenu: callback for VIDIOC_QUERYMENU ioctl handler code.
 *
 * @ioctl: called at the end of ioctl() syscall handler at the V4L2 core.
 *         used to provide support for private ioctls used on the driver.
 *
 * @compat_ioctl32: called when a 32 bits application uses a 64 bits Kernel,
 *                  in order to fix data passed from/to userspace.
 *
 * @g_register: callback for VIDIOC_G_REGISTER ioctl handler code.
 *
 * @s_register: callback for VIDIOC_G_REGISTER ioctl handler code.
 *
 * @s_power: puts subdevice in power saving mode (on == 0) or normal operation
 *      mode (on == 1).
 *
 * @interrupt_service_routine: Called by the bridge chip's interrupt service
 *      handler, when an interrupt status has be raised due to this subdev,
 *      so that this subdev can handle the details.  It may schedule work to be
 *      performed later.  It must not sleep.  *Called from an IRQ context*.
 *
 * @subscribe_event: used by the drivers to request the control framework that
 *                   for it to be warned when the value of a control changes.
 *
 * @unsubscribe_event: remove event subscription from the control framework.
 *
 * @registered_async: the subdevice has been registered async.
 *
 * This is a copy&paste of a more complexe struct, just for testing.
 */
struct v4l2_subdev_core_ops {
        int (*log_status)(struct v4l2_subdev *sd);
        int (*s_io_pin_config)(struct v4l2_subdev *sd, size_t n,
                                      struct v4l2_subdev_io_pin_config *pincfg);
        int (*init)(struct v4l2_subdev *sd, u32 val);
        int (*load_fw)(struct v4l2_subdev *sd);
        int (*reset)(struct v4l2_subdev *sd, u32 val);
        int (*s_gpio)(struct v4l2_subdev *sd, u32 val);
        int (*queryctrl)(struct v4l2_subdev *sd, struct v4l2_queryctrl *qc);
        int (*g_ctrl)(struct v4l2_subdev *sd, struct v4l2_control *ctrl);
        int (*s_ctrl)(struct v4l2_subdev *sd, struct v4l2_control *ctrl);
        int (*g_ext_ctrls)(struct v4l2_subdev *sd, struct v4l2_ext_controls *ctrls);
        int (*s_ext_ctrls)(struct v4l2_subdev *sd, struct v4l2_ext_controls *ctrls);
        int (*try_ext_ctrls)(struct v4l2_subdev *sd, struct v4l2_ext_controls *ctrls);
        int (*querymenu)(struct v4l2_subdev *sd, struct v4l2_querymenu *qm);
        long (*ioctl)(struct v4l2_subdev *sd, unsigned int cmd, void *arg);
#ifdef CONFIG_COMPAT
        long (*compat_ioctl32)(struct v4l2_subdev *sd, unsigned int cmd,
                               unsigned long arg);
#endif
#ifdef CONFIG_VIDEO_ADV_DEBUG
        int (*g_register)(struct v4l2_subdev *sd, struct v4l2_dbg_register *reg);
        int (*s_register)(struct v4l2_subdev *sd, const struct v4l2_dbg_register *reg);
#endif
        int (*s_power)(struct v4l2_subdev *sd, int on);
        int (*interrupt_service_routine)(struct v4l2_subdev *sd,
                                                u32 status, bool *handled);
        int (*subscribe_event)(struct v4l2_subdev *sd, struct v4l2_fh *fh,
                               struct v4l2_event_subscription *sub);
        int (*unsubscribe_event)(struct v4l2_subdev *sd, struct v4l2_fh *fh,
                                 struct v4l2_event_subscription *sub);
        int (*registered_async)(struct v4l2_subdev *sd);
};

/**
 * DOC: Media Controller
 *
 * The media controller userspace API is documented in DocBook format in
 * Documentation/DocBook/media/v4l/media-controller.xml. This document focus
 * on the kernel-side implementation of the media framework.
 *
 * * Abstract media device model:
 *
 * Discovering a device internal topology, and configuring it at runtime, is one
 * of the goals of the media framework. To achieve this, hardware devices are
 * modelled as an oriented graph of building blocks called entities connected
 * through pads.
 *
 * An entity is a basic media hardware building block. It can correspond to
 * a large variety of logical blocks such as physical hardware devices
 * (CMOS sensor for instance), logical hardware devices (a building block
 * in a System-on-Chip image processing pipeline), DMA channels or physical
 * connectors.
 *
 * A pad is a connection endpoint through which an entity can interact with
 * other entities. Data (not restricted to video) produced by an entity
 * flows from the entity's output to one or more entity inputs. Pads should
 * not be confused with physical pins at chip boundaries.
 *
 * A link is a point-to-point oriented connection between two pads, either
 * on the same entity or on different entities. Data flows from a source
 * pad to a sink pad.
 *
 *
 * * Media device:
 *
 * A media device is represented by a struct &media_device instance, defined in
 * include/media/media-device.h. Allocation of the structure is handled by the
 * media device driver, usually by embedding the &media_device instance in a
 * larger driver-specific structure.
 *
 * Drivers register media device instances by calling
 *	__media_device_register() via the macro media_device_register()
 * and unregistered by calling
 *	media_device_unregister().
 *
 * * Entities, pads and links:
 *
 * - Entities
 *
 * Entities are represented by a struct &media_entity instance, defined in
 * include/media/media-entity.h. The structure is usually embedded into a
 * higher-level structure, such as a v4l2_subdev or video_device instance,
 * although drivers can allocate entities directly.
 *
 * Drivers initialize entity pads by calling
 *	media_entity_pads_init().
 *
 * Drivers register entities with a media device by calling
 *	media_device_register_entity()
 * and unregistred by calling
 *	media_device_unregister_entity().
 *
 * - Interfaces
 *
 * Interfaces are represented by a struct &media_interface instance, defined in
 * include/media/media-entity.h. Currently, only one type of interface is
 * defined: a device node. Such interfaces are represented by a struct
 * &media_intf_devnode.
 *
 * Drivers initialize and create device node interfaces by calling
 *	media_devnode_create()
 * and remove them by calling:
 *	media_devnode_remove().
 *
 * - Pads
 *
 * Pads are represented by a struct &media_pad instance, defined in
 * include/media/media-entity.h. Each entity stores its pads in a pads array
 * managed by the entity driver. Drivers usually embed the array in a
 * driver-specific structure.
 *
 * Pads are identified by their entity and their 0-based index in the pads
 * array.
 * Both information are stored in the &media_pad structure, making the
 * &media_pad pointer the canonical way to store and pass link references.
 *
 * Pads have flags that describe the pad capabilities and state.
 *
 *	%MEDIA_PAD_FL_SINK indicates that the pad supports sinking data.
 *	%MEDIA_PAD_FL_SOURCE indicates that the pad supports sourcing data.
 *
 * NOTE: One and only one of %MEDIA_PAD_FL_SINK and %MEDIA_PAD_FL_SOURCE must
 * be set for each pad.
 *
 * - Links
 *
 * Links are represented by a struct &media_link instance, defined in
 * include/media/media-entity.h. There are two types of links:
 *
 * 1. pad to pad links:
 *
 * Associate two entities via their PADs. Each entity has a list that points
 * to all links originating at or targeting any of its pads.
 * A given link is thus stored twice, once in the source entity and once in
 * the target entity.
 *
 * Drivers create pad to pad links by calling:
 *	media_create_pad_link() and remove with media_entity_remove_links().
 *
 * 2. interface to entity links:
 *
 * Associate one interface to a Link.
 *
 * Drivers create interface to entity links by calling:
 *	media_create_intf_link() and remove with media_remove_intf_links().
 *
 * NOTE:
 *
 * Links can only be created after having both ends already created.
 *
 * Links have flags that describe the link capabilities and state. The
 * valid values are described at media_create_pad_link() and
 * media_create_intf_link().
 *
 * Graph traversal:
 *
 * The media framework provides APIs to iterate over entities in a graph.
 *
 * To iterate over all entities belonging to a media device, drivers can use
 * the media_device_for_each_entity macro, defined in
 * include/media/media-device.h.
 *
 * 	struct media_entity *entity;
 *
 * 	media_device_for_each_entity(entity, mdev) {
 * 		// entity will point to each entity in turn
 * 		...
 * 	}
 *
 * Drivers might also need to iterate over all entities in a graph that can be
 * reached only through enabled links starting at a given entity. The media
 * framework provides a depth-first graph traversal API for that purpose.
 *
 * Note that graphs with cycles (whether directed or undirected) are *NOT*
 * supported by the graph traversal API. To prevent infinite loops, the graph
 * traversal code limits the maximum depth to MEDIA_ENTITY_ENUM_MAX_DEPTH,
 * currently defined as 16.
 *
 * Drivers initiate a graph traversal by calling
 *	media_entity_graph_walk_start()
 *
 * The graph structure, provided by the caller, is initialized to start graph
 * traversal at the given entity.
 *
 * Drivers can then retrieve the next entity by calling
 *	media_entity_graph_walk_next()
 *
 * When the graph traversal is complete the function will return NULL.
 *
 * Graph traversal can be interrupted at any moment. No cleanup function call
 * is required and the graph structure can be freed normally.
 *
 * Helper functions can be used to find a link between two given pads, or a pad
 * connected to another pad through an enabled link
 *	media_entity_find_link() and media_entity_remote_pad()
 *
 * Use count and power handling:
 *
 * Due to the wide differences between drivers regarding power management
 * needs, the media controller does not implement power management. However,
 * the &media_entity structure includes a use_count field that media drivers
 * can use to track the number of users of every entity for power management
 * needs.
 *
 * The &media_entity.@use_count field is owned by media drivers and must not be
 * touched by entity drivers. Access to the field must be protected by the
 * &media_device.@graph_mutex lock.
 *
 * Links setup:
 *
 * Link properties can be modified at runtime by calling
 *	media_entity_setup_link()
 *
 * Pipelines and media streams:
 *
 * When starting streaming, drivers must notify all entities in the pipeline to
 * prevent link states from being modified during streaming by calling
 *	media_entity_pipeline_start().
 *
 * The function will mark all entities connected to the given entity through
 * enabled links, either directly or indirectly, as streaming.
 *
 * The &media_pipeline instance pointed to by the pipe argument will be stored
 * in every entity in the pipeline. Drivers should embed the &media_pipeline
 * structure in higher-level pipeline structures and can then access the
 * pipeline through the &media_entity pipe field.
 *
 * Calls to media_entity_pipeline_start() can be nested. The pipeline pointer
 * must be identical for all nested calls to the function.
 *
 * media_entity_pipeline_start() may return an error. In that case, it will
 * clean up any of the changes it did by itself.
 *
 * When stopping the stream, drivers must notify the entities with
 *	media_entity_pipeline_stop().
 *
 * If multiple calls to media_entity_pipeline_start() have been made the same
 * number of media_entity_pipeline_stop() calls are required to stop streaming.
 * The &media_entity pipe field is reset to NULL on the last nested stop call.
 *
 * Link configuration will fail with -%EBUSY by default if either end of the
 * link is a streaming entity. Links that can be modified while streaming must
 * be marked with the %MEDIA_LNK_FL_DYNAMIC flag.
 *
 * If other operations need to be disallowed on streaming entities (such as
 * changing entities configuration parameters) drivers can explicitly check the
 * media_entity stream_count field to find out if an entity is streaming. This
 * operation must be done with the media_device graph_mutex held.
 *
 * Link validation:
 *
 * Link validation is performed by media_entity_pipeline_start() for any
 * entity which has sink pads in the pipeline. The
 * &media_entity.@link_validate() callback is used for that purpose. In
 * @link_validate() callback, entity driver should check that the properties of
 * the source pad of the connected entity and its own sink pad match. It is up
 * to the type of the entity (and in the end, the properties of the hardware)
 * what matching actually means.
 *
 * Subsystems should facilitate link validation by providing subsystem specific
 * helper functions to provide easy access for commonly needed information, and
 * in the end provide a way to use driver-specific callbacks.
 */
