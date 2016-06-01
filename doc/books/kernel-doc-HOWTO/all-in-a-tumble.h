/* parse-markup: reST */


/**
 * struct my_struct - short description
 * @a: first member
 * @b: second member
 *
 * Longer description
 */
struct my_struct {
  int a;
  int b;
  /**
   * @c: This is longer description of C
   *
   * You can use paragraphs to describe arguments
   * using this method.
   */
  int c;
};






/**
 * DOC: kernel-doc reST markup test
 *
 * This file is a dummy to test kernel-doc markup. Here you will also find some
 * copy&paste from the linux kernel sources. Don't look to close, it is just for
 * testing kernel-doc and reST markup.
 *
 * This description is only to test some reST inline markups like *emphasise*
 * and **bold**. The follwing is a test of a reST list markup:
 *
 * - item one
 * - item two
 *
 * - item three with
 *   a linebreak
 *
 * The next example shows a literal block::
 *
 *     +------+          +------+
 *     |\     |\        /|     /|
 *     | +----+-+      +-+----+ |
 *     | |    | |      | |    | |
 *     +-+----+ |      | +----+-+
 *      \|     \|      |/     |/
 *       +------+      +------+
 *
 *
 * The next example shows a code example, with highlighting C syntax in the
 * output.
 *
 * .. code-block:: c
 *
 *     // Hello World program
 *
 *     #include<stdio.h>
 *
 *     int main()
 *     {
 *         printf("Hello World");
 *     }
 *
 */


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
