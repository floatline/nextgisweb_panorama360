import { FieldsForm, useForm } from "@nextgisweb/gui/fields-form";
import { useEffect, useState, useMemo } from "react";
import { ContentBox } from "@nextgisweb/gui/component/ContentBox";
import i18n from "@nextgisweb/pyramid/i18n!gui";


export const Panorama360Plugin = ({ url }) => {




  console.log("i work");
  console.log(url)
  return (
    <div className="ngw-panorama360-webmap-plugin" style={{ padding: "16px" }}>
      <h1>Panorama360 Webmap</h1>
      <div>{url}</div>
    </div>
  );
};
