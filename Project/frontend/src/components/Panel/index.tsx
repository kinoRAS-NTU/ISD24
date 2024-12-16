import type { FC } from 'react'
import { ListGroup, type ListGroupProps } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'

import type { ObjectId } from '@/types/drawing'
import type { State } from '@/types/state'

import PanelItem from './Item'
import Object from './Object'

const Panel: FC<ListGroupProps> = ({ ...restProps }) => {
    const tool = useSelector((state: State) => state.tool)
    const currentObject = useSelector((state: State) => state.currentObject)
    const finishedObjects = useSelector((state: State) => state.finishedObjects[tool])
    const isolatedObjectId = useSelector((state: State) => state.isolatedObjectId)

    const dispatch = useDispatch()

    const handleIsolateClick = (id: ObjectId) =>
        dispatch({ type: 'ISOLATE_OBJECT', payload: isolatedObjectId === id ? undefined : id })

    const handleDeleteClick = (id: ObjectId) => dispatch({ type: 'DELETE_OBJECT', payload: { tool, id } })

    return (
        <ListGroup data-bs-theme="dark" {...restProps}>
            <PanelItem name="Current Drawing">
                <Object object={currentObject} isCurrent />
            </PanelItem>
            <PanelItem name="Finished Drawings">
                {finishedObjects.map((object) => (
                    <Object
                        key={object.id}
                        object={object}
                        onIsolateClick={() => handleIsolateClick(object.id)}
                        onDeleteClick={() => handleDeleteClick(object.id)}
                    />
                ))}
            </PanelItem>
        </ListGroup>
    )
}

export default Panel