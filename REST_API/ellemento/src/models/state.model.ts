import {Entity, model, property, hasMany} from '@loopback/repository';
import {TrayMovement} from './tray-movement.model';

@model({settings: {strict: false}})
export class State extends Entity {
  @property({
    type: 'number',
    id: true,
    generated: true,
  })
  state_id?: number;

  @property({
    type: 'number',
    required: true,
  })
  state_type_id: number;

  @property({
    type: 'number',
    required: true,
  })
  batch_id: number;

  @property({
    type: 'number',
  })
  batchId?: number;

  @hasMany(() => TrayMovement)
  trayMovements: TrayMovement[];
  // Define well-known properties here

  // Indexer property to allow additional data
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  [prop: string]: any;

  constructor(data?: Partial<State>) {
    super(data);
  }
}

export interface StateRelations {
  // describe navigational properties here
}

export type StateWithRelations = State & StateRelations;
