import type { FC } from 'react'
import { ListGroup, type ListGroupProps } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'

import type { ObjectId } from '@/types/drawing'
import type { State } from '@/types/state'

import FrameEntry from './Frame'
import PanelItem from './Item'
import ObjectEntry from './Object'

const Panel: FC<ListGroupProps> = ({ ...restProps }) => {
    const tool = useSelector((state: State) => state.tool)
    const currentObject = useSelector((state: State) => state.currentObject)
    const finishedObjects = useSelector((state: State) => state.finishedObjects[tool])
    const isolatedObjectId = useSelector((state: State) => state.isolatedObjectId)

    const dispatch = useDispatch()

    const handleEditClick = (id: ObjectId) => dispatch({ type: 'EDIT_OBJECT', payload: id })

    const handleIsolateClick = (id: ObjectId) =>
        dispatch({ type: 'ISOLATE_OBJECT', payload: isolatedObjectId === id ? undefined : id })

    const handleDeleteClick = (id: ObjectId) => dispatch({ type: 'DELETE_OBJECT', payload: id })

    return (
        <ListGroup data-bs-theme="dark" style={{ display: 'flex', flexDirection: 'column' }} {...restProps}>
            <PanelItem name="Current Drawing">
                <ObjectEntry object={currentObject} isCurrent>
                    {tool === 'Flipbook' && (
                        <ListGroup style={{ marginBlock: 4 }}>
                            {currentObject.frames.map((frame, index) => (
                                <FrameEntry key={index} index={index} frame={frame} />
                            ))}
                        </ListGroup>
                    )}
                </ObjectEntry>
            </PanelItem>
            <PanelItem name="Finished Drawings" style={{ flex: 1 }}>
                {finishedObjects.map((object) => (
                    <ObjectEntry
                        key={object.id}
                        object={object}
                        onEditClick={() => handleEditClick(object.id)}
                        onIsolateClick={() => handleIsolateClick(object.id)}
                        onDeleteClick={() => handleDeleteClick(object.id)}
                    />
                ))}
            </PanelItem>
        </ListGroup>
    )
}

export default Panel
