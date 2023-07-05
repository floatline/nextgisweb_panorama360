import { Button, Modal } from "@nextgisweb/gui/antd";
import { useRef, useLayoutEffect } from "react";
import i18n from "@nextgisweb/pyramid/i18n!gui";
import showModal from "@nextgisweb/gui/showModal"
import "pannellum"

import "./Panorama360Modal.less"
import "pannellum/build/pannellum.css"

const PannellumModal = ({ url, ...props }) => {

    const pannellumWrapper = useRef(null);
    console.log(typeof (url));

    useLayoutEffect(() => {
        pannellumWrapper.current = window.pannellum.viewer(pannellumWrapper.current, {
            autoLoad: true,
            type: "equirectangular",
            panorama: url
        });
        return () => {
            pannellumWrapper.current.destroy()
        }
    }, []);

    return (
        <Modal
            title={null}
            width="70%"
            height="80%"
            closable={true}
            centered={true}
            footer={null}
            {...props}
        >
            <div
                height="100%"
                width="fit-content"
                ref={pannellumWrapper}
            >

            </div>

        </Modal >
    )
};

export const Panorama360Display = ({ url, _open }) => {

    return (<div className="ngw-panorama360-identify-button"
        centered="true"
    >
        <Button
            centered="true"
            onClick={() => {
                const modal = showModal(PannellumModal, {
                    url,
                    onCancel: e => {
                        modal.destroy();
                    }
                })
            }}
        >
            {i18n.gettext("Open panorama")}
        </Button>

    </div>)
};
