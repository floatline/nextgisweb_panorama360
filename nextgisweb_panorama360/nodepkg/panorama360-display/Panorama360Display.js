import { Button, Tabs, Modal, Upload, Checkbox } from "@nextgisweb/gui/antd";
import { useEffect, useState, useMemo, useRef, useLayoutEffect } from "react";
import { ContentBox } from "@nextgisweb/gui/component/ContentBox";
import i18n from "@nextgisweb/pyramid/i18n!gui";
import showModal from "@nextgisweb/gui/showModal"
import "pannellum"

import "./Panorama360Modal.less"
import "pannellum/build/pannellum.css"

const PannellumModal = ({ url, ...props }) => {
    const pannellumWrapper = useRef(null);

    useLayoutEffect(() => {
        if (pannellumWrapper.current) {
            window.pannellum.viewer(pannellumWrapper.current, {
                "type": "equirectangular",
                {pannellumWrapper.current}: { url }
            });
        }
        return () => { 
            
        }
        //TODO: unmount pannellum
    }, []);

    return (
        <Modal
            title={null}
            width="900px"
            height="600px"
            closable={true}
            centered={true}
            footer={null}
            {...props}
        >
            <div
                height="600px"
                width="900px"
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
