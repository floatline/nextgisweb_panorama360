import { FieldsForm, useForm} from "@nextgisweb/gui/fields-form";
import { useEffect, useState } from "react";
import i18n from "@nextgisweb/pyramid/i18n!gui"
//, values, setValues, initLoading

export const Panorama360 = observer(([store]) =>  {
     

    const form = useForm()[0];

    const [enabled, setEnabled] = useState(false);
    const [panorama360LayerField, setPanorama360LayerField] = useState();
    // const [values, setValues] = useState();



    

    const fields = useMemo(() => [
        {
            name: "enabled",
            title: i18n.gettext("Enable Panorama360"),
            widget: "checkbox",
            required: true,
        },
        {
            name: "panorama360LayerField",
            title: i18n.gettext("Select the name of the field where the panorama links are"),
            required: true,
            disabled: !enabled,
            widget: "input"
        }
    ],
    // [enabled, panorama360LayerField]
    [enabled]
    );
    
    const p = { fields, size: "large", form };

    useEffect(() => {
         console.log(store);
     }, []);

    // const updateField()

    const onChange = (val) => {
        setPanorama360LayerField((oldVal) => ({oldval, val.value}));
    };

    return (
        <div>
            <FieldsForm>
                {p}
                onChange={onChange}
            </FieldsForm>
        </div>
    );
}

    
    
);


